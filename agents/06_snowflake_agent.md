[« 制御エージェント v2](./05_controlled_agent2.md)

# 概要

前回の学びをさらに活かして、もっと**自由度を下げて**＋**実運用で使える具体的なタスク**に当ててみる

つまり：

> 自動エージェントで Snowflake クエリを書いてもらえないか？

理由は：

- 人間はやりたいことがわかってるけど、それを実装するのが億劫という、 LLM にかなり適したケース
- 大量のデータ（Trinity のログのドキュメント）があるけど、それを裏で持っていて LLM に少しずつ絞っていってもらうのができるのでは？

# 流れ（理想）

**プロンプト**：〜〜をするクエリが欲しい。コンテンツログとアクションログがある。コンテンツログに動画、生放送、ユーザー etc. の情報がある。アクションログに視聴イベント、いいね etc. の情報がある。その内どれが必要そう？

**LLM**：動画に関するコンテンツログと視聴イベントに関するアクションログ

**プロンプト**：動画に関するコンテンツログは（関連するテーブルのリストとそれぞれの短い説明）、視聴イベントに関するアクションログは etc.

**LLM**：このテーブルとこのテーブルが使いたい

**プロンプト**：それらのテーブルはこういう定義でこういうカラムを持っていて etc.

**LLM**：（完成したクエリ）

# 実験

1. エンべディング＋ベクトルサーチで実装（キーワードをつけるのは一旦保留）
2. サーチで取得したテーブルをさらに LLM に関連性順にリランキングしてもらう
3. 一番関連性のありそうなテーブルから、さらに LLM にカラムを絞ってもらう（トークン数オーバーせずに複数のテーブルを同時に LLM に見せられるように）
4. 一番関連性のありそうなテーブルの一番重要そうなカラムだけを、いくつか同時に LLM に見せてクエリを書いてもらう

## 実験１：マイリスの割合

### 入力

> 直近１ヶ月でアクティブなユーザーの視聴した動画の何割をマイリストしたのか？

### 出力

```sql
WITH active_users AS (
  SELECT DISTINCT user_id
  FROM niconico.common_action.common_action_watch_event_v3
  WHERE DATE(event_time) BETWEEN DATEADD(MONTH, -1, CURRENT_DATE()) AND CURRENT_DATE()
), watched_videos AS (
  SELECT DISTINCT user_id, content_id
  FROM niconico.common_action.common_action_watch_event_v3
  WHERE DATE(event_time) BETWEEN DATEADD(MONTH, -1, CURRENT_DATE()) AND CURRENT_DATE()
), videos_in_mylist AS (
  SELECT user_id, content_id
  FROM niconico.specific_action.specific_action_nicovideo_mylistedit_v2
  WHERE action_type = 'add' AND item_type = 'video'
), watched_and_mylist AS (
  SELECT active_users.user_id, watched_videos.content_id, videos_in_mylist.user_id AS in_mylist
  FROM active_users
  JOIN watched_videos ON active_users.user_id = watched_videos.user_id
  LEFT JOIN videos_in_mylist ON watched_videos.user_id = videos_in_mylist.user_id AND watched_videos.content_id = videos_in_mylist.content_id
)
SELECT COUNT(DISTINCT CASE WHEN in_mylist IS NOT NULL THEN watched_and_mylist.content_id END) / COUNT(DISTINCT watched_and_mylist.content_id) AS percentage_mylist
FROM watched_and_mylist
```

パーティション用の `AND dt BETWEEN '20230501' AND '20230601'` を追加したらエラーなしにこのクエリを実行できた。ただし結果はそれぞれのユーザーに対してではなく、全体の集計だった。入力が少し曖昧だったようだけど嬉しい結果ではある。

`GROUP BY user_id` を追加したら（多分）正しい結果になる。

## 実験２：マイリスの割合修正版

### 入力

> 直近１ヶ月でアクティブなユーザーそれぞれに対して、視聴した動画の何割をマイリストしたのか？

### 出力 ①

```sql
SELECT
  w.user_id_nohash,
  COUNT(DISTINCT w.content_id) AS videos_watched,
  COUNT(DISTINCT m.content_id) AS videos_added_to_mylist,
  COUNT(DISTINCT m.content_id) / COUNT(DISTINCT w.content_id) AS percentage_added_to_mylist
FROM
  niconico.common_action.common_action_watch_event_v3 w
  JOIN niconico.content.content_nicovideo_mylistfollow_v1 m
    ON w.content_id = m.content_id
  JOIN niconico.content.content_nicovideo_video_v2 v
    ON w.content_id = v.content_id
WHERE
  w.additional_parameters LIKE '%\"player_version\":\"html5\"%' -- filter for HTML5 views only
  AND DATEADD('MONTH', -1, CURRENT_DATE()) <= TRY_CAST(REGEXP_REPLACE(TO_VARCHAR(upload_datetime, 'YYYY-MM-DD'),'-','') AS DATE) -- filter for events within the last month
GROUP BY
  w.user_id_nohash
ORDER BY
  percentage_added_to_mylist DESC;
```

不正なクエリだった。そもそも mylistfollow に content_id フィールドがないし、mylistfollow の意味を勘違いしているようだ。あと `TRY_CAST(REGEXP_REPLACE(...` のところも Syntax Error が出る。

### 出力 ②

```sql
SELECT
  event.user_id,
  COUNT(DISTINCT event.content_id) AS total_views,
  ROUND(COUNT(DISTINCT mylist.content_id) / COUNT(DISTINCT event.content_id), 4) AS mylist_ratio
FROM niconico.common_action.common_action_watch_event_v3 AS event
LEFT JOIN niconico.content.content_nicovideo_video_v2 AS mylist ON event.content_id = mylist.content_id AND mylist.mylist_num > 0
WHERE event.event_time >= DATEADD(DAY, -30, GETDATE()) -- Limit to the last month
GROUP BY event.user_id;
```

今回はエラーなしだが、「そのユーザーがマイリスしたもの」ではなく、「誰かのマイリスに入っている動画」を集計してしまっている。

LLM の出力を見ると、一番の問題点は、ステップ２の時、役に立っていたであろう `specific_action.nicovideo_mylistedit` を、存在しない `content.nicovideo_mylistedit` と言ってしまい、ステップ３以降そのテーブルの情報が一切入ってこなかったこと。

### 出力 ③

少しだけいじってみた。テーブル名を間違えることがあったので、検索結果それぞれをインデックスと紐づけて、 LLM にインデックスを選択してもらう。ただの数字だと間違いが減るのでは、と思ったけど…

実験では、根拠の文章では「`mylistedit` が役に立ちそう」と言ったのに、`mylistedit` のインデックスを最終的に選択しなかった。

しかし今回は割とうまくいった。

```sql
SELECT
    watch.user_id,
    COUNT(DISTINCT watch.content_id) AS total_videos_watched,
    COUNT(DISTINCT mylist.content_id) AS videos_added_to_mylist,
    COUNT(DISTINCT mylist.content_id) / COUNT(DISTINCT watch.content_id) AS mylist_percentage
FROM niconico.common_action.common_action_watch_event_v3 AS watch
LEFT JOIN niconico.content.content_nicovideo_mylist_v1 AS mylist
    ON watch.user_id = mylist.user_id AND watch.content_id = mylist.content_id
WHERE DATE_FROM_PARTS(TO_INTEGER(SUBSTRING(watch.event_time, 1, 4)), TO_INTEGER(SUBSTRING(watch.event_time, 6, 2)), TO_INTEGER(SUBSTRING(watch.event_time, 9, 2))) >= DATEADD(MONTH, -1, CURRENT_DATE())
GROUP BY watch.user_id;
```

`dt` を手動で追加しないといけないけど、以前成功したクエリよりシンプルで正しそうな結果を返す。ただし `TO_INTEGER` は Snowflake にないので、 `TO_NUMBER` に変える必要があった。 SQL は Snowflake だけ書いてくださいって指示はしている。

### 出力 ④

```sql
SELECT
  user_id_nohash,
  SUM(CASE WHEN mylist_event.content_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS percentage_mylist
FROM
  niconico.common_action.common_action_watch_event_v3 AS watch_event
LEFT JOIN (
  SELECT DISTINCT
    content_id,
    user_id_nohash
  FROM
    niconico.content.content_nicovideo_mylist_v1
  WHERE
    create_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
) AS mylist_event ON
  watch_event.content_id = mylist_event.content_id AND
  watch_event.user_id_nohash = mylist_event.user_id_nohash
WHERE
  watch_event.event_type = 'play' AND
  watch_event.dt >= TO_VARCHAR(DATEADD('day', -30, CURRENT_TIMESTAMP()), 'YYYYMMDD')
GROUP BY
  user_id_nohash
ORDER BY
  percentage_mylist DESC;
```

`SQL compilation error: ambiguous column name 'USER_ID_NOHASH'` エラーが出るけど、それを手動で修正するとちゃんとエラーなしで実行できて正しそうな結果を返す。`dt` も、プロンプトに説明を入れたらちゃんと使ってくれている。

## 実験３：フォローしたユーザーの投稿動画の視聴率

### 入力

> 直近１ヶ月でアクティブなユーザーそれぞれに対して、視聴した動画の何割がフォローしているユーザーが投稿した動画ですか？

### 苦戦した点

- タスクの意図を勘違いする（思考過程を書かせても）
- 投稿者の情報を得るに必要な content_nicovideo_video_v2 テーブルを取得しない
  - ベクトル検索で出てこなかったけど、検索のやり方を変えたら出るようになった
  - 具体的に、検索に与える情報量を逆に減らした。LLM に必要そうな情報をリストアップしてもらって、それぞれの情報だけで検索をかけて、最後に一つのリストにまとめた
- 意味のわからない SQL （謎のセルフジョインなど）
  - 書いてもらった根拠が正しくても SQL がおかしくなることもある
- 要らないテーブルを使ってしまう
  - 情報を多めに出している（経験上、必要なテーブルが必ずトップ n に入る保証はない）ので使わなくていい情報も使ってしまう（フォローユーザーを集計したいのにマイリスを使ってしまう）

### 出力例

```sql
-- Get active users who have watched videos in the last month
WITH active_users AS (
  SELECT DISTINCT user_id_nohash
  FROM niconico.common_action.common_action_watch_event_v3
  WHERE dt >= DATEADD(MONTH, -1, CURRENT_DATE())
),

-- Calculate the number of watched videos per user
user_content AS (
  SELECT user_id_nohash, COUNT(*) AS viewed_content_count
  FROM niconico.common_action.common_action_watch_event_v3
  WHERE dt >= DATEADD(MONTH, -1, CURRENT_DATE())
  GROUP BY user_id_nohash
),

-- Calculate the number of watched videos per user that were posted by the users they follow
user_follow_content AS (
  SELECT
    event.user_id_nohash,
    COUNT(DISTINCT event.content_id) AS followed_content_count
  FROM niconico.common_action.common_action_watch_event_v3 AS event
    JOIN niconico.content.content_nicovideo_video_v2 AS video
      ON event.content_id = video.content_id
    JOIN niconico.content.content_saussure_followuser_v2 AS follow
      ON event.user_id_nohash = follow.user_id_nohash
      AND video.user_id = follow.followed_user_id_nohash
  WHERE event.dt >= DATEADD(MONTH, -1, CURRENT_DATE())
  GROUP BY event.user_id_nohash
)

-- Join to get the user's viewed video count and followed video count
SELECT
  active_users.user_id_nohash,
  user_content.viewed_content_count,
  user_follow_content.followed_content_count,
  user_follow_content.followed_content_count / user_content.viewed_content_count AS fraction_followed_content
FROM active_users
  JOIN user_content ON active_users.user_id_nohash = user_content.user_id_nohash
  LEFT JOIN user_follow_content ON active_users.user_id_nohash = user_follow_content.user_id_nohash;
```

問題点

- そもそも `dt` で絞っているから、`active_users` は不要（あっても正しく実行できるけど）
- `dt` は 'YYYYMMDD' 形式じゃないといけない
- `user_id` と `user_id_nohash` をジョインしようとしている
- `user_content` にある `COUNT(*)` は正しくは `COUNT(DISTINCT content_id)`
- フォローユーザーの動画を視聴していない場合、 `NULL` を `0` に変換すべき
