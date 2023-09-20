[« 自動 Snowflake 改善 4](./04_auto_snowflake3.md)

# テンプレート変数を挿入して Fine-Tuning

- テンプレート変数を全部ありそうな値で挿入して再学習
- さらに学習データと評価データをランダムサンプリングする（非常に似ているクエリがあったので）

## 例 1

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/daikoku-batch/blob/master/daikoku/template/channel2channel_followed.sql

### プロンプト（生成）

以下の要件を満たす SQL クエリを作成してください。

- 集計対象の期間は 2021 年 9 月 1 日以降（20210901）
- 公式番組を放送しているチャンネル（`content_nicolive_channelofficialmap_v1`テーブル）
- 生放送を行っているチャンネル（`content_nicolive_live_v1`テーブル）
- 動画を投稿しているチャンネル（`content_nicovideo_video_v2`テーブル）
- ブロマガを更新しているチャンネル（`content_nicochannel_blomaga_v1`テーブル）

上記の条件を満たすアクティブなチャンネルのリストを作成し、それぞれのチャンネルをフォローしているユーザーを集計してください。集計結果は、ユーザーごとにフォローしているチャンネルのリストとして表示してください。

### 正解（実際のクエリ）

```sql
with public_live_channel as (
    select
        distinct channelofficialmap.channel_id as channel_id
    from
        content.content_nicolive_channelofficialmap_v1 as channelofficialmap
        join content.content_nicolive_live_v1 as nicolive on nicolive.provider_type = 'official'
        and channelofficialmap.content_id = nicolive.contents_id
        and nicolive.dt >= '20210901'
),
channel_live_channel as (
    select
        distinct cast(replace(default_community_id, 'ch', '') as int) channel_id
    from
        content.content_nicolive_live_v1
    where
        provider_type = 'channel'
        and dt >= '20210901'
        and default_community_id like 'ch%%'
),
channel_video_channel as (
    select
        distinct channel_id
    from
        content.content_nicovideo_video_v2
    where
        provider_type = 'channel'
        and channel_id != -1
        and upload_datetime > '2021-09-01T00:00:00+09:00'
),
channel_blomaga_channel as (
    select
        distinct channel_id
    from
        content.content_nicochannel_blomaga_v1
    where
        official_flag = 1
        and public_flag = 0
        and penalty_flag = 0
        and update_datetime > '2021-09-01T00:00:00+09:00'
),
active_channel as (
    select
        distinct channel.channel_id as channel_id
    from
        content.content_nicochannel_channel_v1 as channel
        left outer join public_live_channel as public_live_channel on channel.channel_id = public_live_channel.channel_id
        left outer join channel_live_channel as channel_live_channel on channel.channel_id = channel_live_channel.channel_id
        left outer join channel_video_channel as channel_video_channel on channel.channel_id = channel_video_channel.channel_id
        left outer join channel_blomaga_channel as channel_blomaga_channel on channel.channel_id = channel_blomaga_channel.channel_id
    where
        channel.hidden_flag = 0
        and channel.category_id != 14
        and (
            public_live_channel.channel_id is not null
            or channel_live_channel.channel_id is not null
            or channel_video_channel.channel_id is not null
            or channel_blomaga_channel.channel_id is not null
        )
)
select
    COLLECT_LIST(cast(follow.channel_id as string)) as contents_ids
from
    content.content_nicochannel_followuser_v1 as follow
    inner join active_channel on follow.channel_id = active_channel.channel_id
    and follow.create_datetime < '2021-10-01T00:00:00+09:00'
group by
    follow.user_id
```

一応古い Hive クエリである（なぜか Sqlfluff はエラーを吐かなかった）

### Fine-tuning なし（関数あり）

```sql
SELECT uf.user_id, ARRAY_AGG(DISTINCT uf.channel_id) AS followed_channels
FROM content_nicochannel_followuser_v1 uf
JOIN (
  SELECT ch.channel_id
  FROM content_nicolive_channelofficialmap_v1 ch_off
  JOIN content_nicochannel_channel_v1 ch
  ON ch_off.channel_id = ch.channel_id
  UNION
  SELECT ch.channel_id
  FROM content_nicolive_live_v1 l
  JOIN content_nicochannel_channel_v1 ch
  ON l.channel_id = ch.channel_id
  WHERE l.create_datetime >= '2021-09-01'
  UNION
  SELECT ch.channel_id
  FROM content_nicovideo_video_v2 v
  JOIN content_nicochannel_channel_v1 ch
  ON v.channel_id = ch.channel_id
  WHERE v.upload_datetime >= '2021-09-01'
  UNION
  SELECT ch.channel_id
  FROM content_nicochannel_blomaga_v1 b
  JOIN content_nicochannel_channel_v1 ch
  ON b.channel_id = ch.channel_id
  WHERE b.update_datetime >= '2021-09-01'
) c
ON uf.channel_id = c.channel_id
GROUP BY uf.user_id
```

**感想**

- 日付の形式が違う（ただし文字列比較としては間違ってはない）
- JOIN じゃなくて UNION なのが多分違う？

### Fine-tuning あり（関数未対応）

```sql
WITH
active_channel AS (
    SELECT
        channel_id, 'live' AS provider_type
    FROM
        content.content_nicolive_channelofficialmap_v1 cf JOIN content.content_nicolive_live_v1 l ON cf.content_id = l.official_program_id
    WHERE
        TO_DATE('2013-09-01' || 'T00:00:00+09:00') < CF.UPLOAD_DATETIME

    UNION

    SELECT
        channel_id, 'video' AS provider_type
    FROM
        content.content_nicovideo_video_v2 v JOIN content.content_nicolive_channelofficialmap_v1 cf ON cf.content_id = v.fx
    WHERE
        TO_DATE('2013-09-01' || 'T00:00:00+09:00') < TO_DATE(v.upload_datetime)
        AND v.provider_type = 'channel'

    UNION

    SELECT
        channel_id, 'blomaga' AS provider_type
    FROM
        content.content_nicochannel_blomaga_v1
    WHERE
        TO_DATE('2013-09-01' || 'T00:00:00+09:00') < TO_DATE(update_datetime)
        AND (official_flag > 0 OR penalty_flag = 0) AND public_flag = 1

),

cutoff AS (
    SELECT TO_DATE('2013-09-01'), TO_DATE('2013-10-01')
)

SELECT
    f.user_id AS user_id,
    LISTAGG(DISTINCT c.channel_id, ',') WITHIN GROUP (ORDER BY c.channel_id) AS interested_channels
FROM (
    SELECT DISTINCT user_id FROM content.content_nicochannel_followuser_v1
) AS f
CROSS JOIN cutoff AS t
JOIN active_channel AS c ON t.start_date < c.provider_type AND c.provider_type < t.end_date AND c.channel_id IN (
    SELECT DISTINCT channel_id FROM content.content_nicolive_channelofficialmap_v1
)
GROUP BY f.user_id

```

**感想**

- cutoff がおかしい（そもそもカラムに名前がついてないのでエラーになる）
- provider_type が違うけどそれは一部プロンプトのせい（content_nicolive_live_v1 のテーブルのドキュメントをちゃんと入れてなかった）
- こちらも JOIN じゃなくて UNION を使っている
- 当たり前だけど変数がなくなった
- 日付は正しそう

## 例 2

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/virtual_follow/blob/master/virtual_follow/templates/snowflake/live/aggregate.sql

### プロンプト（生成）

以下の条件に基づいて、2021 年 10 月 1 日から 2021 年 10 月 31 日の間に、20 分以上視聴時間があり、コンテンツ提供元タイプが'community'、公開ステータスが'public'であり、視聴しているユーザーがフォローしていないユーザーの関係を抽出するクエリを書いてください。結果は最大 500 行まで表示してください。抽出する情報は、暗号化されたユーザー ID とフォローされているユーザー ID のペアです。

### 正解（実際のクエリ）

```sql
WITH
watch AS (
    SELECT DISTINCT
        watch_interactions.user_id,
        watch_interactions.score,
        content.content_nicolive_live_v2.user_id AS followed_user_id,
        content.content_nicolive_live_v2.content_id
    FROM
        (
            SELECT
                user_id,
                content_id,
                CASE
                    WHEN total_watch_milliseconds >= 20 * 60 * 1000 THEN 3  -- 20 minutes
                    WHEN total_watch_milliseconds >= 10 * 60 * 1000 THEN 2  -- 10 minutes
                    ELSE 1
                END AS score -- 視聴時間について可変なスコアを割り振る
            FROM summary.content_watch_milliseconds
            WHERE
                dt BETWEEN '20211001' AND '20211031'
                AND total_watch_milliseconds > 180000 -- 180秒以上視聴しているレコードに限定
        ) AS watch_interactions
    INNER JOIN content.content_nicolive_live_v2
        ON watch_interactions.content_id = content.content_nicolive_live_v2.content_id
    WHERE
        content.content_nicolive_live_v2.dt BETWEEN '20211001' AND '20211031'
        AND content.content_nicolive_live_v2.provider_type = 'community'
        AND content.content_nicolive_live_v2.public_status = 'public'
        AND content.content_nicolive_live_v2.user_id != watch_interactions.user_id
),

watch_count AS (
    SELECT
        user_id,
        followed_user_id,
        SUM(score) AS score
    FROM watch
    GROUP BY user_id, followed_user_id
),

virtual_follow AS (
    SELECT
        watch_count.user_id,
        watch_count.followed_user_id
    FROM watch_count
    LEFT OUTER JOIN content.content_saussure_followuser_v2
        ON
            watch_count.user_id = content.content_saussure_followuser_v2.user_id
            AND watch_count.followed_user_id = content.content_saussure_followuser_v2.followed_user_id
    WHERE
        watch_count.score >= 100
        AND content.content_saussure_followuser_v2.followed_user_id IS NULL
)

SELECT
    TO_NUMBER(e1.plaintext) AS user_id,
    TO_NUMBER(e2.plaintext) AS followed_user_id
FROM virtual_follow
INNER JOIN
    content.content_enigma AS e1
    ON e1.ciphertext = virtual_follow.user_id
INNER JOIN
    content.content_enigma AS e2
    ON e2.ciphertext = virtual_follow.followed_user_id
LIMIT 500;

```

### Fine-tuning なし（関数あり）

```sql
SELECT DISTINCT l.user_id, f.followed_user_id
FROM niconico.content.content_nicolive_live_v2 l
JOIN niconico.content.content_saussure_followuser_v2 f ON l.user_id = f.user_id
WHERE l.dt BETWEEN '20211001' AND '20211031'
  AND l.provider_type = 'community'
  AND l.public_status = 'public'
  AND l.watch_time >= 1200
LIMIT 500;
```

**感想**

- だいぶ短い（プロンプトのせいかも）
- dt はちゃんとしている（プロンプトでは説明しているけど普通は言うことを聞かないことが多い）

### Fine-tuning あり（関数未対応）

```sql
-- 2021年10月1日から2021年10月31日の間に、20分以上視聴時間があり、コンテンツ提供元タイプが'community'、公開ステータスが'public'であり、視聴しているユーザーがフォローしていないユーザーの関係
-- 同一ユーザーによる重複フォローは存在しえないため排除する
SELECT DISTINCT to_follow.user_id AS to_follow, follower.user_id AS follower
FROM niconico.content.content_nicolive_live_v2 content
INNER JOIN niconico.content.content_saussure_followuser_v2 to_follow
ON content.user_id = to_follow.followed_user_id
INNER JOIN niconico.content.content_saussure_followuser_v2 follower
ON follower.user_id = to_follow.user_id
WHERE content.dt BETWEEN '20211001' AND '20211031'
AND content.provider_type = 'community'
AND content.public_status = 'public'
AND to_follow.user_id != follower.user_id
AND content.content_id != 'chXXXXXXXX'
-- たかだか20分以上の番組を視聴したことがある
AND content.content_id IN (
  SELECT p.content_id
  FROM (
    SELECT
      temp.content_id,
      nvl(temp1.listen_duration_sec, 0) AS listen_duration_sec,
      row_number() OVER (PARTITION BY temp.content_id ORDER BY nvl(temp1.listen_duration_sec, 0) DESC) AS r
    FROM rni.merge_with_1dv.content p
    INNER JOIN rni.mingl.sherlock_filtered_tag_summary_v1 temp
      ON temp.content_id = p.reason_id
    INNER JOIN rni.azusa.content.raw_behavior_test
      ON to_number(convert_from(base64decode(querystring), 'UTF8')) = temp.content_id
    LEFT OUTER JOIN rni.azusa.content.vv_to_content_quartile_sold_sec_test_view temp1
      ON temp1.content_id = temp.content_id
        AND temp1.watch_id = watch_id
    WHERE
        user_id = 'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
      AND temp.source = 'azusa_v2'
      AND temp.tag_general_score > 0.2
    QUALIFY r = 1
  )
  WHERE listen_duration_sec >= 20 * 60
)
AND
  to_follow.dt BETWEEN tig0.id AND to_char(to_date(tig0.id) + 6, 'YYYYMMDD')
AND
  from_follow.dt BETWEEN tig0.id AND to_char(to_date(tig0.id) + 6, 'YYYYMMDD')

```

**感想**

- user_id がどうした？！？！？
- というか色々おかしい（存在しないテーブルも）

## 例 3

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/rena-batch/blob/master/misc/sql/get_user_access_log.sql

### プロンプト（生成）

指定期間内（例えば 2018 年 8 月 8 日から 2018 年 9 月 8 日）に最低 100 回以上視聴したユーザーのアクセスログを取得するクエリを書いてください。取得する情報はユーザー ID、視聴コンテンツ ID、アクセス時間です。また、結果はユーザー ID の昇順およびアクセス時間の降順でソートしてください。なお、ユーザー ID はハッシュ化されていますが、ユーザー ID の昇順でソートすることで、ユーザーごとのアクセスログを分かりやすく表示できます。

### 正解（実際のクエリ）

```sql
WITH row_watch_log
AS (
    SELECT
        common_action.common_action_watch_event_v3.user_id_nohash,
        common_action.common_action_watch_event_v3.content_id,
        common_action.common_action_watch_event_v3.watch_track_id,
        MIN(common_action.common_action_watch_event_v3.time) AS access_time,
        IFF(common_action.common_action_watch_event_v3.frontend_id = 1,
            SUM(common_action.common_action_watch_event_v3.watch_milliseconds),
            MAX(common_action.common_action_watch_event_v3.watch_milliseconds)
        ) AS watch_time
    FROM common_action.common_action_watch_event_v3
    INNER JOIN content.content_nicovideo_video_v2
        ON content.content_nicovideo_video_v2.content_id
           = common_action.common_action_watch_event_v3.content_id
    WHERE common_action.common_action_watch_event_v3.dt BETWEEN '20180808' AND '20180908'
        AND common_action.common_action_watch_event_v3.content_id LIKE 'sm%%'
        AND common_action.common_action_watch_event_v3.user_id_nohash != 'guest'
    GROUP BY
        common_action.common_action_watch_event_v3.user_id_nohash,
        common_action.common_action_watch_event_v3.content_id,
        common_action.common_action_watch_event_v3.frontend_id,
        common_action.common_action_watch_event_v3.watch_track_id
),

video_access_num
AS (
    SELECT
        content_id,
        COUNT(content_id) AS access_num
    FROM row_watch_log
    WHERE watch_time > 300000
    GROUP BY content_id
),

video_log
AS (
    SELECT *
    FROM video_access_num
    WHERE access_num > 300
),

watch_log
AS (
    SELECT
        row_watch_log.user_id_nohash,
        row_watch_log.content_id,
        row_watch_log.access_time,
        ROW_NUMBER() OVER(
            PARTITION BY row_watch_log.user_id_nohash ORDER BY row_watch_log.access_time DESC
        ) AS watch_order
    FROM row_watch_log
    INNER JOIN video_log ON video_log.content_id = row_watch_log.content_id
    WHERE row_watch_log.watch_time > 300000
),

user_watch_count
AS (
    SELECT
        user_id_nohash,
        MAX(watch_order) AS watch_count
    FROM watch_log GROUP BY user_id_nohash
)

SELECT
    watch_log.user_id_nohash,
    watch_log.content_id,
    watch_log.access_time
FROM watch_log
INNER JOIN user_watch_count ON user_watch_count.user_id_nohash = watch_log.user_id_nohash
WHERE user_watch_count.watch_count >= 100
      AND watch_log.watch_order <= 5000
ORDER BY watch_log.user_id_nohash ASC, watch_log.access_time DESC

```

### Fine-tuning なし（関数あり）

```sql
SELECT user_id_nohash, content_id, time
FROM niconico.common_action.common_action_watch_event_v3 w
JOIN niconico.content.content_nicovideo_video_v2 c
ON w.content_id = c.content_id
WHERE dt >= '2018-08-08' AND dt <= '2018-09-08'
GROUP BY user_id_nohash, content_id, time
HAVING COUNT(*) >= 100
ORDER BY user_id_nohash ASC, time DESC;
```

**感想**

- TODO

### Fine-tuning あり（関数未対応）

```sql
-- selected_period = '20180808' to '20180908'
-- watch_threshold = 100
-- remove_duplicates = true

WITH filtered AS (
  SELECT
    user_id_nohash AS user_id,
    content_nicovideo_video_v2.content_id AS content_id,
    MAX(time) AS time
  FROM niconico.common_action.common_action_watch_event_v3
  INNER JOIN
    niconico.content.content_nicovideo_video_v2
    ON common_action_watch_event_v3.content_id =
       content_nicovideo_video_v2.content_id
  WHERE dt BETWEEN '20180801' AND '20180908'
    AND watch_milliseconds > 0
  GROUP BY
    common_action_watch_event_v3.user_id_nohash,
    common_action_watch_event_v3.content_id
)

SELECT
  f.user_id AS user_id,
  f.content_id AS content_id,
  module.user_time2utc(f.time) AS access_time
FROM filtered f
INNER JOIN niconico_misc.user_session_session:ss
  ON f.user_id = ss.user_id
INNER JOIN niconico_misc.user_session_time2utc:module
  ON ss.session_id = module.session_id
WHERE
    (
      dateadd(day, -1, current_timestamp())
        AT TIME ZONE 'UTC'
    )
    <= datetime
AND datetime
       <= current_timestamp()
    AT TIME ZONE 'Asia/Tokyo'
  AND (
    :remove_duplicates = TRUE
    OR (
      f.user_id,
      f.content_id,
      module.user_time2utc(f.time)
)
      NOT IN (
        SELECT content_id,
               imp_user_id,
               to_number(imp_time),
               access_time0
        FROM bi_batch.collab_filter_collab_filter_result
        WHERE
                   imp_user_id IS NOT NULL
          AND imp_item_id
          IN (SELECT full_id
              FROM dig_scaler_scheduler.uitable)
      )
    )
ORDER BY
  user_id ASC,
  access_time DESC
```

**感想**

- TODO
