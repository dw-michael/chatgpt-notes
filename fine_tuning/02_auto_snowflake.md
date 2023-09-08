[« Fine-tuning 触ってみた](./01_sat_questions.md) | [自動 Snowflake 改善 2 »](./03_auto_snowflake2.md)

# 自動 Snowflake 改善

以前作った自動 Snowflake クエリ生成システム： http://amadeus.kurisu.nico:30722/

やりたいことを入力したら、 AI が自動的に Trinity を使ったクエリを生成してくれる。

実際使われている Snowflake クエリを用いて fine-tuning したら性能が良くなるかも？つまり AI に、こういう入力に対して、こういうクエリが正解、という例を見せる。

# 難点

- fine-tuning はまだ関数に対応していない（対応する予定があるらしい）
- 学習例の「正解」（実際使われているクエリ）があるとしたら、きれいな「入力」（これがやりたかったからこのクエリを書いた）がない
- つまりそれぞれのクエリに対して、「やっていること」の説明が必要

# 手法

- yaoyorozu の GitHub から sql ファイルをクローリング（Trinity のテーブル名を含む ＋ Snowflake としてパース可能なもののみ）
- 結果： 117 件のクエリを取得
- それぞれのクエリの使用するテーブル、フィールドを抽出
- クエリの目的を GPT に要約してもらう **← 今ここ**
- その要約と対応するクエリで学習例を作って fine-tuning する

# 擬似入力生成

改めて説明すると、 fine-tuning したい流れは：

```
ユーザー：〇〇をするクエリを書きたい
AI：これはいかがでしょう： SELECT xxx FROM yyy etc.
```

クローリングした sql が AI の返事になるけど、ユーザーの入力に相当するものがない（レポの README から多少は汲み取れるけどクエリ一つ一つに対応するものがない）。

なので 117 件のクエリを人間が読んで手動で要約を書くか、GPT に書かせるかのどっちかになる。もちろん後者が効率的。

上の流れのユーザー入力になるような文章を書いてもらうには、どういうプロンプトがいい？と少し試行錯誤したら以下のプロンプトになった：

```
【System】
あなたはニコニコ動画などのサービスを運営する株式会社ドワンゴの新入社員の研修を手伝うアシスタント

新入社員は社内データベースの使い方を学んでいる。社内データベースは Big Brother (BB) または Trinity と呼ばれている。このデータベースは Snowflake SQL を使っている

以下は現在の社員が書いたクエリとクエリに使われているテーブルの説明。クエリにテンプレート変数が組み込まれている可能性があるが、それらは使用時に値が与えられるものとする

このクエリは研修の課題の答えになる。このクエリが答えになるような課題を書いてください


【User】
以下のクエリを書かせるような課題を作ってください。このクエリは答えの例であり、研修生には見せられない

クエリ：
{sql}

{table_documentation}

このクエリは以下の社内アプリで使われている：
{readme}
```

# 出力例

## 例 1

出典： https://github.o-in.dwango.co.jp/yaoyorozu/amano-iwato-batch/blob/master/amano_iwato_batch/templates/select_live_table.sql

クエリ：

```sql
SELECT content_id                                                        AS contents_id,
       IFF(watch_num = -1, 0, watch_num)                                 AS watch_num,
       IFF(title = 'null', NULL, title)                                  AS title,
       TO_CHAR(register_datetime::DATETIME, 'yyyy-MM-ddTHH:mm:ss')       AS create_time,
       IFF(update_datetime = '3000-01-01T00:00:00+09:00', NULL,
           TO_CHAR(update_datetime::DATETIME, 'yyyy-MM-ddTHH:mm:ss'))    AS update_time,
       IFF(start_datetime = '3000-01-01T00:00:00+09:00', NULL,
           TO_CHAR(start_datetime::DATETIME, 'yyyy-MM-ddTHH:mm:ss'))     AS start_time,
       IFF(end_datetime = '3000-01-01T00:00:00+09:00', NULL,
           TO_CHAR(end_datetime::DATETIME, 'yyyy-MM-ddTHH:mm:ss'))       AS end_time,
       2                                                                 AS live_cycle,
       IFF(public_status = 'public', 0, 1)                               AS public_status,
       IFF(invisible_datetime = '3000-01-01T00:00:00+09:00', NULL,
           TO_CHAR(invisible_datetime::DATETIME, 'yyyy-MM-ddTHH:mm:ss')) AS invisible_time,
       CASE provider_type
           WHEN 'official' THEN channel_id
           WHEN 'channel' THEN channel_id
           ELSE user_id_nohash
           END                                                           AS uid,
       CASE provider_type
           WHEN 'official' THEN 0
           WHEN 'channel' THEN 1
           ELSE 2
           END                                                           AS provider_type,
       CASE provider_type
           WHEN 'official' THEN channel_id
           WHEN 'channel' THEN channel_id
           ELSE community_id
           END                                                           AS social_id,
       IFF(comment_num = -1, 0, comment_num)                             AS comment_num,
       NULL                                                              AS category
FROM niconico.content.content_nicolive_live_v2
WHERE dt BETWEEN '{begin}' AND '{end}'
```

GPT の出力：

```
ニコニコ生放送の生放送情報ログから、指定した期間（{begin}から{end}）のデータを取得するクエリを作成してください。結果セットには、番組ID、タイトル、開始時刻、終了時刻、来場者数の情報を含めてください。2つのテーブルを結合して必要な情報を取得する必要があります。また、日付のフォーマットを'yyyy-MM-ddTHH:mm:ss'に変換してください。
```

余談： GPT-4 に書かせたらもっと詳しく正確に書いてくれたけど、コストと時間がすごかったので、とりあえず GPT-3.5 で試している

## 例 2

出典： https://github.o-in.dwango.co.jp/yaoyorozu/amano-iwato-batch/blob/master/amano_iwato_batch/templates/select_live_tag.sql

クエリ：

```sql
WITH tags AS (
             SELECT content_id,
                    ARRAY_CAT(
                        IFF(category_tags = 'null', ARRAY_CONSTRUCT(), SPLIT(category_tags, ' ')),
                        IFF(lock_tags = 'null', ARRAY_CONSTRUCT(), SPLIT(lock_tags, ' '))
                        ) AS tags
             FROM niconico.content.content_nicolive_live_v2
             WHERE dt BETWEEN '{begin}' AND '{end}'
)
SELECT DISTINCT content_id,
                tag.value::STRING AS tag,
                NULL              AS normalize
FROM tags,
     LATERAL FLATTEN(INPUT => tags.tags) tag
```

GPT の出力：

```
ニコニコ生放送の生放送情報ログから、指定の期間内の生放送番組に使用された全てのカテゴリタグとロックタグを表示してください。結果に含まれるタグは一意になるようにしてください。
```

## 例 3

出典： https://github.o-in.dwango.co.jp/yaoyorozu/mie/blob/master/batch/mie_batch/daily/query_ctr_engine.sql

クエリ：

```sql
WITH app AS (
  SELECT *
  FROM specific_action.specific_action_recommend_app_v1
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ display_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_app_v1.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ display_end_time.isoformat(timespec="seconds") }}'
),
display AS (
  SELECT time, recommend_id, recommend_content_id
  FROM specific_action.specific_action_recommend_display_v2
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ display_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_display_v2.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ display_end_time.isoformat(timespec="seconds") }}'
  UNION
  SELECT TO_TIMESTAMP_TZ(time), recommend_id, contents_id
  FROM specific_action.specific_action_recommend_display_v1
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ display_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_display_v1.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ display_end_time.isoformat(timespec="seconds") }}'
),
content AS (
  SELECT *
  FROM specific_action.specific_action_recommend_content_v1
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ display_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_content_v1.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ display_end_time.isoformat(timespec="seconds") }}'
),
response AS (
  SELECT time, recommend_id, recommend_content_id
  FROM specific_action.specific_action_recommend_response_v2
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ response_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_response_v2.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ response_end_time.isoformat(timespec="seconds") }}'
  UNION
  SELECT TO_TIMESTAMP_TZ(time), recommend_id, recommend_contents_id
  FROM specific_action.specific_action_recommend_response_v1
  WHERE dt BETWEEN '{{ display_begin_time.strftime("%Y%m%d") }}' AND '{{ response_end_time.strftime("%Y%m%d") }}'
    AND specific_action_recommend_response_v1.time BETWEEN '{{ display_begin_time.isoformat(timespec="seconds") }}' AND '{{ response_end_time.isoformat(timespec="seconds") }}'
),
all_merged AS (
  SELECT
    app.request_site,
    content.engine,
    app.recommend_id,
    CASE
      WHEN datediff(second, display.time, response.time) <= {{ response_timeout.total_seconds() | int }} THEN 1
      ELSE 0
    END click
  FROM app
  JOIN content ON app.recommend_id = content.recommend_id
  JOIN display ON app.recommend_id = display.recommend_id AND content.content_id = display.recommend_content_id
  LEFT JOIN response ON app.recommend_id = response.recommend_id AND display.recommend_content_id = response.recommend_content_id
),
unique_count_by_engine AS (
  SELECT
    request_site,
    engine,
    recommend_id,
    max(click) click
  FROM all_merged
  GROUP BY
    request_site,
    engine,
    recommend_id
)
SELECT
  request_site,
  engine,
  count(*) AS engine_display_count,
  sum(click) AS engine_click_count
FROM unique_count_by_engine
GROUP BY
  request_site,
  engine
;
```

GPT の出力：

```
テーブル `niconico.specific_action.specific_action_recommend_app_v1`、`niconico.specific_action.specific_action_recommend_content_v1`、`niconico.specific_action.specific_action_recommend_display_v1`、`niconico.specific_action.specific_action_recommend_display_v2`、`niconico.specific_action.specific_action_recommend_response_v1`、`niconico.specific_action.specific_action_recommend_response_v2` を使って、以下の情報を集計するクエリを作成してください。

- リクエストサイトごとの表示回数とクリック回数を集計し、表示回数とクリック回数の合計を表示してください。
- エンジンごとの表示回数とクリック回数を集計し、表示回数とクリック回数の合計を表示してください。
- 全体の表示回数とクリック回数を表示してください。

なお、以下の条件で集計することとします。
- レコメンドシステムのリクエストの対象期間: `display_begin_time` から `display_end_time`
- レコメンドシステムのレスポンスの対象期間: `display_begin_time` から `response_end_time`
- クリックされた場合のレスポンスのタイムアウト: `response_timeout`

クエリのテンプレート変数を適切に埋め込んでください。
```
