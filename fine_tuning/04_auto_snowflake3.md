[« 自動 Snowflake 改善 3](./03_auto_snowflake2.md)

# 学習データ修正

学習データ一つ一つを人間の目である程度確認し、プロンプトをそれに合わせ工夫して再生成を行なった。結果も全部目で確認した上モデルを再学習。

# 全体的な感想

- 存在しないテーブルがなくなったけど、まだ変なところに妄想が？
- 微妙に不正なシンタックスが増えた気がする
- クエリの後半で目的を見失うことはまだ多い
- デモで使ってみたとき、学習データによくあるテンプレート変数を、プロンプトで与えなくても勝手に入れていた

## 例 1

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/holmes-batch-v2/blob/master/templates/custom_ranking.sql

### 正解（実際のクエリ）

```sql
with videos as (
    select distinct(content_id) from content.content_nicovideo_video_v2
    where upload_datetime >= '{{ datetime_ago(log_target_days, "%Y-%m-%dT%H:%M:%S+09:00") }}'
),
tag as (
    select content_id, regular_tag as tag
    from content.content_nicovideo_tag_v1
    where
        regular_tag != '【タグ編集ハデキマセン】' and
        regular_tag != '投稿者コメント' and
        regular_tag != 'ニコニ・コモンズ' and
        regular_tag != '＠BGM推奨' and
        regular_tag != 'ニコニコムービーメーカー' and
        content_id in (select content_id from videos)
),
tag_freq as (  -- (tag, tag-frequency)
    select tag, count(*) as cnt from tag group by tag
),
pair as (  -- 同じ動画に共起するタグのペアすべて
    select tag1.tag as t1, tag2.tag as t2
    from tag tag1
    inner join tag tag2 on tag1.content_id = tag2.content_id and tag1.tag != tag2.tag
),
pair_freq as (
    select t1, t2, count(*) as cnt from pair group by t1, t2
),
tag_simpson as (
    select
        t1, t2, pair_freq.cnt as c, tag1.cnt as c1, tag2.cnt as c2,
        (pair_freq.cnt / tag1.cnt) as simpson  -- #pair(t1, t2) / min(#t1, #t2)
    from pair_freq
    inner join tag_freq tag1 on pair_freq.t1 = tag1.tag
    inner join tag_freq tag2 on pair_freq.t2 = tag2.tag
    where tag1.cnt < tag2.cnt and tag1.cnt > 0
),
result as (
    select t1, t2, c, c1, c2, simpson,
           row_number() over (partition by t1 order by c2 asc) as rnk
    from tag_simpson
    where
        simpson >= {{ min_simpson }}
        and c >= {{ min_pair_count }}
        and c1 >= {{ min_tag_count }}
        and c2 >= {{ min_tag_count }}
)
select t1 as child, t2 as parent from result where rnk = 1

```

### Fine-tuning なし

前章を参照

### Fine-tuning あり（関数未対応）

```sql
-- タグの共起関係を計算するクエリ
-- 子タグの頻度を数え、関連性の高いタグのペアを抽出する。
-- 子タグは全体のTAG_RATE_IN_CONTENTSが下回るものを選ぶ。

WITH TAGS_DATA AS (
    SELECT DISTINCT
        CNT.content_id AS CONTENT_ID,
        T.regular_tag AS TAG
    FROM content.content_nicovideo_video_v2 CNT
    JOIN content.content_nicovideo_tag_v1 T
        ON CNT.content_id = T.content_id
    WHERE
        CNT.upload_datetime >= TO_TIMESTAMP(
            '{XDAYSAGO}-09-01 00:00:00', 'YYYY-MM-DD HH24:MI:SS'
        )
        AND T.regular_tag NOT IN (
            '', -- 空文字
            '.+', -- ニコニコ動画メーカー
            'ニコニ・コモンズ', -- ニコニ・コモンズ
            '+', -- BGM推奨
            'ニコニコムービーメーカー' -- ニコニコムービーメーカー
        )
        AND T.regular_tag:!ALL:全体のTAG_RATE_IN_CONTENTS
            OR T.regular_tag IN (SELECT M.INTERSECTION
                                 FROM content.tmp_tag_popularity M
                                 WHERE M.DATE =
                                     TO_TIMESTAMP(
                                         '{XDAYSAGO}-09-01 00:00:00', 'YYYY-MM-DD HH24:MI:SS'
                                     )))
,
TAG_POPULARITY AS (
    SELECT
        TAG,
        COUNT(DISTINCT CONTENT_ID) AS COUNT
    FROM TAGS_DATA
    GROUP BY TAG
    HAVING COUNT(DISTINCT CONTENT_ID) >= :mincl
)
,
TAG_POPULARITY_ALL AS (
    SELECT
        TAG,
        COUNT(DISTINCT CONTENT_ID) AS COUNT
    FROM TAGS_DATA
    GROUP BY TAG
)

SELECT
    PALL.TAG AS PARENT,
    CNT.TAG AS CHILD
FROM TAGS_DATA CNT
    INNER JOIN-
    TAG_POPULARITY P ON CNT.TAG = P.TAG
    INNER JOIN-
    TAG_POPULARITY_ALL PAL ON CNT.TAG = PAL.TAG
WHERE
    P.COUNT != 0
    AND PALL.COUNT != 0
    AND (P.COUNT / PALL.COUNT) < :TAG_RATE_IN_CONTENTS

```

**感想**

- 存在しないテーブルはなくなったが、やはり何かと妄想が入っている（プロンプトになかった変数、 regular_tag NOT IN のフィルターのわけがわからないタグ）
- SQL シンタックスも怪しいところが？（`INNER JOIN-` とか）
- タグのカウントまではできたんだけど、肝心な共起率の計算は見られない

## 例 2

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/holmes-batch-v2/blob/master/templates/nicobox.sql

### 正解（実際のクエリ）

```sql
with nicobox_videos as (
    select distinct(content_id)
    from common_action.common_action_watch_event_v3
    where
        frontend_id in (75, 76) and content_type = 'video' and event_type = 'start'
        and dt >= '{{ datetime_ago(log_target_days) }}'
),
tag as (
    select content_id, regular_tag as tag
    from content.content_nicovideo_tag_v1
    where
        regular_tag != '【タグ編集ハデキマセン】' and
        regular_tag != '投稿者コメント' and
        regular_tag != 'ニコニ・コモンズ' and
        regular_tag != '＠BGM推奨' and
        regular_tag != 'ニコニコムービーメーカー' and
        content_id in (select content_id from nicobox_videos)
),
tag_freq as (  -- (tag, tag-frequency)
    select tag, count(*) as cnt from tag group by tag
),
pair as (  -- 同じ動画に共起するタグのペアすべて
    select tag1.tag as t1, tag2.tag as t2
    from tag tag1
    inner join tag tag2 on tag1.content_id = tag2.content_id and tag1.tag != tag2.tag
),
pair_freq as (
    select t1, t2, count(*) as cnt from pair group by t1, t2
),
tag_simpson as (
    select
        t1, t2, pair_freq.cnt as c, tag1.cnt as c1, tag2.cnt as c2,
        (pair_freq.cnt / tag1.cnt) as simpson  -- #pair(t1, t2) / min(#t1, #t2)
    from pair_freq
    inner join tag_freq tag1 on pair_freq.t1 = tag1.tag
    inner join tag_freq tag2 on pair_freq.t2 = tag2.tag
    where tag1.cnt < tag2.cnt and tag1.cnt > 0
),
result as (
    select t1, t2, c, c1, c2, simpson,
           row_number() over (partition by t1 order by c2 asc) as rnk
    from tag_simpson
    where
        simpson >= {{ min_simpson }}
        and c >= {{ min_pair_count }}
        and c1 >= {{ min_tag_count }}
        and c2 >= {{ min_tag_count }}
)
select t1 as child, t2 as parent from result where rnk = 1

```

### Fine-tuning なし

前章を参照

### Fine-tuning あり（関数未対応）

```sql
WITH unique_actions AS (
    SELECT
        distinct_content_id AS content_id,
        unique_modified FROM
        (SELECT
            content_id,
            modified,
            ROW_NUMBER()
                OVER (PARTITION BY content_id
                    ORDER BY modified DESC)
                unique_modified FROM
                niconico.common_action.common_action_watch_event_v3
                WHERE
                    dt BETWEEN '{start_date}' AND '{end_date}'
                    AND event_type = 'end'
                    AND content_type = 'video'
                )  ON modified = unique_modified)
),

tags AS (
    SELECT content_id, regular_tag AS tag
    FROM niconico.content.content_nicovideo_tag_v1
    WHERE dt BETWEEN '{start_date}' AND '{end_date}'
      AND regular_tag != ''),

tags_per_video AS (
    SELECT
        content_id,
        COUNT(DISTINCT tag) AS n_tags,
        LISTAGG(DISTINCT tag, ',') WITHIN GROUP (ORDER BY tag ASC) AS csv_tags
    FROM tags
    GROUP BY content_id),

pair_count AS (
    SELECT
        split_part(csv_tags, ',', 1) AS tag1,
        split_part(csv_tags, ',', 2) AS tag2,
        content_id
    FROM tags_per_video
    WHERE n_tags >= {min_count}),

n_tags AS (
    SELECT tag, COUNT(DISTINCT content_id) AS n_videos
    FROM (SELECT tag1 AS tag, content_id FROM pair_count
          UNION ALL
          SELECT tag2 AS tag, content_id FROM pair_count)
    GROUP BY tag),

final AS (
    SELECT a.tag1, a.tag2, a.content_id
    FROM (SELECT
            pair_count.*,
            {min_count} AS n
          FROM pair_count
              JOIN n_tags t1 ON pair_count.tag1 = t1.tag
         WHERE t1.n_videos >= {min_count}) a
        JOIN n_tags t2 ON a.tag2 = t2.tag AND t2.n_videos >= a.n)

SELECT
    final.tag1,
    final.tag2,
    COUNT(DISTINCT final.content_id) AS n_co_views
FROM final
GROUP BY final.tag1, final.tag2
HAVING n_co_views >= least({max_count}, GREATEST(1, final.n_co_views(
    final.content_id,

    {max_count}, {min_count}))))
}

SELECT
    tag1,
    tag2,
    n_co_views
FROM (
    {inner_query})
ORDER BY n_co_views DESC
LIMIT {limit}
;

```

**感想**

- Fine-tuning なしの時にもあった謎の inner_query
- カッコが不対象など、シンタックスも怪しい

## 例 3

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/holmes-batch-v2/blob/master/templates/trend_tag.sql

### 正解（実際のクエリ）

```sql
WITH videos AS (
    SELECT
        content_nicovideo_video_v2.content_id,
        content_nicovideo_video_v2.watch_num,
        content_nicovideo_tag_v1.regular_tag
    FROM niconico.content.content_nicovideo_video_v2
    INNER JOIN niconico.content.content_nicovideo_tag_v1 ON content_nicovideo_tag_v1.content_id = content_nicovideo_video_v2.content_id
    WHERE TO_DATE(content_nicovideo_video_v2.upload_datetime) >= CURRENT_DATE - {{ interval_days }}
)

SELECT
    regular_tag,
    SUM(watch_num) AS score
FROM videos
GROUP BY regular_tag
HAVING COUNT(DISTINCT content_id) >= {{ num_video }}

```

### Fine-tuning なし（関数なし）

クエリを書かなかった（説明を書いただけ）

### Fine-tuning なし（関数あり）

```sql
WITH recent_videos AS (
  SELECT *
  FROM niconico.content.content_nicovideo_video_v2
  WHERE upload_datetime >= DATEADD(DAY, -{{ interval_days }}, CURRENT_TIMESTAMP)
    AND watch_num >= {{ num_video }}
)

SELECT regular_tag, SUM(watch_num) AS score
FROM recent_videos
JOIN niconico.content.content_nicovideo_tag_v1
  ON recent_videos.content_id = niconico.content.content_nicovideo_tag_v1.content_id
GROUP BY regular_tag
ORDER BY score DESC
```

**感想**

- 簡単な方のクエリだけど、なかなかいいのでは？ `SELECT *` だけが少し気になるけど悪くはない

### Fine-tuning あり（関数未対応）

```sql
-- Get popular tags based on the number of video views
-- You can limit tags to those used on videos uploaded within the last {{ interval_days }} days
-- and that have a video view count of at least {{ num_video }}

WITH popular_videos AS (
  SELECT *
    FROM niconico.content.content_nicovideo_video_v2
   WHERE upload_datetime >= '{{ target_day.isoformat() }}'::timestamp - interval '1 days' * {{ interval_days }}
     AND watch_num >= {{ num_video }}
)

SELECT t.regular_tag, SUM(v.watch_num) AS score
  FROM niconico.content.content_nicovideo_tag_v1 t
  JOIN popular_videos v ON t.content_id = v.content_id
 GROUP BY t.regular_tag

```

**感想**

- `INTERVAL` で掛け算ができないのでシンタックスエラーが発生する
- ただしそれ以外は上と同じくほぼあっている

## 例 4

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/holmes-batch-v2/blob/master/templates/video.sql

### 正解（実際のクエリ）

```sql
with tag as (
    select content_id, regular_tag as tag from content.content_nicovideo_tag_v1
    where
        regular_tag != '【タグ編集ハデキマセン】' and
        regular_tag != '投稿者コメント' and
        regular_tag != 'ニコニ・コモンズ' and
        regular_tag != '＠BGM推奨' and
        regular_tag != 'ニコニコムービーメーカー'
),
tag_freq as (  -- (tag, tag-frequency)
    select tag, count(*) as cnt from tag group by tag
),
pair as (  -- 同じ動画に共起するタグのペアすべて
    select tag1.tag as t1, tag2.tag as t2
    from tag tag1
    inner join tag tag2 on tag1.content_id = tag2.content_id and tag1.tag != tag2.tag
),
pair_freq as (
    select t1, t2, count(*) as cnt from pair group by t1, t2
),
tag_simpson as (
    select
        t1, t2, pair_freq.cnt as c, tag1.cnt as c1, tag2.cnt as c2,
        (pair_freq.cnt / tag1.cnt) as simpson  -- #pair(t1, t2) / min(#t1, #t2)
    from pair_freq
    inner join tag_freq tag1 on pair_freq.t1 = tag1.tag
    inner join tag_freq tag2 on pair_freq.t2 = tag2.tag
    where tag1.cnt < tag2.cnt and tag1.cnt > 0
),
result as (
    select t1, t2, c, c1, c2, simpson,
           row_number() over (partition by t1 order by c2 asc) as rnk
    from tag_simpson
    where
        simpson >= {{ min_simpson }}
        and c >= {{ min_pair_count }}
        and c1 >= {{ min_tag_count }}
        and c2 >= {{ min_tag_count }}
)
select t1 as child, t2 as parent from result where rnk = 1

```

### Fine-tuning なし（関数なし）

クエリを書かなかった（説明を書いただけ）

### Fine-tuning なし（関数あり）

クエリを書かなかった（理由不明）

### Fine-tuning あり（関数未対応）

```sql
-- タグペアクエリ
-- 【SQL】ニコニコ動画の動画タグ情報ログ（niconico.content.content_nicovideo_tag_v1）から、共起するタグのペアを見つける
--
-- 【翻訳】
-- このクエリは、ニコニコ動画の動画タグ情報ログから共起するタグのペアを見つける。
-- 目的は、共起頻度やシンプソン係数を計算し、関連性の高いタグのペアを抽出することです。
--
WITH ﾀｸﾞ AS (
  SELECT DISTINCT
    content_id,
    CASE
      WHEN regular_tag = '【タグ編集ハデキマセン】' THEN NULL
      WHEN regular_tag = '投稿者コメント' THEN NULL
      WHEN regular_tag = 'ニコニ・コモンズ' THEN NULL
      WHEN regular_tag = '＠BGM推奨' THEN NULL
      WHEN regular_tag = 'ニコニコムービーメーカー' THEN NULL
      ELSE regular_tag
    END tag
  FROM niconico.content.content_nicovideo_tag_v1
  WHERE
    regular_tag != '投稿者コメント' -- デコメ編集タグが含まれることがある
    OR regular_tag IS NULL
) -- regular_tagが投稿者コメントの場合は除外する
SELECT
  t1.tag                  AS child,
  t2.tag                  AS parent,
  COUNT(DISTINCT t2.content_id) AS c,
  COUNT(DISTINCT t1.content_id) AS c1,
  COUNT(DISTINCT t2.content_id) AS c2,
  COUNT(DISTINCT t1.content_id) AS c21,
  COUNT(DISTINCT CASE WHEN t1.content_id = t2.content_id THEN t1.tag END) AS content_count  -- メモリ効率UPのため共起カウント用に追加
FROM ﾀｸﾞ t1
JOIN ﾀｸﾞ t2 ON t1.content_id = t2.content_id AND t1.tag < t2.tag
GROUP BY
t1.tag,
t2.tag
)
SELECT
  child,
  parent,
  c,
  c1,
  c2,
  -- シンプソン係数
  1.0 - (c21 / (c1 - c21 + c2)) AS simpson
FROM ﾀｸﾞペア
WHERE 1 <= c
  AND 1 <= c1
  AND 1 <= c2
  AND 0.3 <= c21 / c1 -- c2/tag1_tag2 ≥ 0.3
ORDER BY c DESC
;
```

**感想**

- またカッコが不対象になっててシンタックスが変
- CTE の名前にカタカナ？！
- タグをフィルターする処理が二重？（部分的）
- シンプソン係数の計算はあるけど違うっぽい？そもそも c21 の集計があってない（c1 と全く同じ）
