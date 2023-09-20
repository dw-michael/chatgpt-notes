[« 自動 Snowflake 改善 3](./03_auto_snowflake2.md) | [自動 Snowflake 改善 5 »](./05_auto_snowflake4.md)

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

## 例 5

**出典：** https://github.o-in.dwango.co.jp/yaoyorozu/popbox-batch/blob/master/sql/nicobox.sql

### 正解（実際のクエリ）

```sql
-- SnowflakeQL for Trinity

with
video_freshness as (
    select
        1 / (1 + exp( timestampdiff('seconds', to_timestamp(upload_datetime), current_timestamp) / (3600 * 24 * 30) - 4.0)) + 0.00001 as freshness,
        content_id
    from niconico.content.content_nicovideo_video_v2
    where
        delete_status = 0
        and exclude_flag = 0
        and current_timestamp(0) > to_timestamp(upload_datetime)
),
nicobox_master as (
    select
        s.content_id,
        t.freshness as weight
    from niconico.common_action.common_action_watch_event_v3 s
    inner join video_freshness t on s.content_id = t.content_id
    where
        dt >= to_varchar(current_date - interval '${log_days} days', 'YYYYmmdd')
        and frontend_id in (75, 76) and event_type = 'start'
),
pop_videos as (
    select content_id, sum(weight) as weight
    from nicobox_master
    group by content_id
),
tag_weight as (
    select regular_tag as tag, t.content_id, weight
    from pop_videos s
    inner join niconico.content.content_nicovideo_tag_v1 t on t.content_id = s.content_id
),
ranking as (
    select tag, content_id, weight, rank() over (partition by tag order by weight desc) as rnk
    from tag_weight
)

select
    tag,
    listagg(content_id, ',') within group (order by rnk asc)
from ranking
where rnk <= ${top_num}
group by tag

```

### Fine-tuning なし（関数なし）※

※レスポンス形式を守らなかった

```sql
WITH ranked_videos AS (
  SELECT
    cvv.content_id,
    cvv.upload_datetime,
    cnt.regular_tag,
    COUNT(*) AS view_count,
    ROW_NUMBER() OVER (PARTITION BY cnt.regular_tag ORDER BY COUNT(*) DESC) AS rank
  FROM niconico.content.content_nicovideo_video_v2 cvv
  INNER JOIN niconico.common_action.common_action_watch_event_v3 caw ON cvv.content_id = caw.content_id
  INNER JOIN niconico.content.content_nicovideo_tag_v1 cnt ON cvv.content_id = cnt.content_id
  WHERE caw.dt >= DATEADD(DAY, -${log_days}, CURRENT_DATE())
  GROUP BY cvv.content_id, cvv.upload_datetime, cnt.regular_tag
)
SELECT regular_tag, ARRAY_AGG(content_id) AS video_ids
FROM ranked_videos
WHERE rank <= ${top_num}
GROUP BY regular_tag
ORDER BY regular_tag;
```

**感想**

- dt の扱いがやはりあってない
- 正解よりだいぶ短いけど意図はあってそう？

### Fine-tuning なし（関数あり）

```sql
WITH
  -- Filter the data based on the specified log_days parameter
  filtered_data AS (
    SELECT
      content_id
    FROM
      niconico.content.content_nicovideo_video_v2
    WHERE
      upload_datetime >= DATEADD(DAY, -${log_days}, CURRENT_DATE())
  ),
  -- Join the video data with tag data
  video_tags AS (
    SELECT
      v.content_id,
      t.regular_tag
    FROM
      niconico.content.content_nicovideo_video_v2 v
    INNER JOIN
      niconico.content.content_nicovideo_tag_v1 t ON v.content_id = t.content_id
    WHERE
      v.content_id IN (SELECT content_id FROM filtered_data)
  ),
  -- Rank the videos by tag based on popularity
  ranked_videos AS (
    SELECT
      regular_tag,
      content_id,
      ROW_NUMBER() OVER (PARTITION BY regular_tag ORDER BY content_id) AS rank
    FROM
      video_tags
  )
SELECT
  regular_tag,
  ARRAY_AGG(content_id) AS video_ids
FROM
  ranked_videos
WHERE
  rank <= ${top_num}
GROUP BY
  regular_tag
```

**感想**

- TODO

### Fine-tuning あり（関数未対応）

```sql
-- ニコニコ動画の人気動画をタグごとにランキングし、各タグごとの動画IDのリストを取得するクエリ

WITH video_ranking AS (
    SELECT content_nicovideo_video_v2.content_id, DENSE_RANK() OVER (ORDER BY c DESC) AS ranking
    FROM niconico.content.content_nicovideo_video_v2
    JOIN (
        SELECT content_id
        FROM niconico.common_action.common_action_watch_event_v3
        WHERE event_type = 'start'
        UNION DISTINCT
        SELECT content_id
        FROM niconico.common_action.common_action_watch_app_v3
        WHERE event_type = 'start'
    ) ON content_nicovideo_video_v2.content_id = content_id
    JOIN (
        SELECT content_id
        FROM niconico.common_action.common_action_watch_event_v3
        WHERE event_type = 'impression'
        AND dt BETWEEN TO_CHAR(TO_DATE('${log_days}', 'yyyymmdd') - 7, 'yyyymmdd') AND '${log_days}'
        UNION DISTINCT
        SELECT content_id
        FROM niconico.common_action.common_action_watch_app_v3
        WHERE event_type = 'impression'
        AND dt BETWEEN TO_CHAR(TO_DATE('${log_days}', 'yyyymmdd') - 7, 'yyyymmdd') AND '${log_days}'
    ) ON content_nicovideo_video_v2.content_id = content_id
    JOIN (
        SELECT content_id
        FROM niconico.content.content_nicovideo_tag_v1
        GROUP BY content_id
        QUALIFY ROW_NUMBER() OVER (PARTITION BY content_id ORDER BY regular_tag) <= 10
    ) ON content_nicovideo_video_v2.content_id = content_id
    CROSS JOIN
        (SELECT content_id, COUNT(*) AS c
        FROM niconico.common_action.common_action_watch_event_v3
        WHERE event_type = 'play'
        AND dt BETWEEN TO_CHAR(TO_DATE('${log_days}', 'yyyymmdd') - 7, 'yyyymmdd') AND '${log_days}'
        GROUP BY content_id
    )
),
tag_log AS (
    SELECT content_id, regular_tag AS tag
    FROM niconico.content.content_nicovideo_tag_v1
    WHERE regular_tag IS NOT NULL
    UNION DISTINCT
    SELECT content_id, action_tag AS tag
n    FROM (
            SELECT content_id, action_tag
                , ROW_NUMBER()
                    OVER (PARTITION BY content_id, action_tag
                          ORDER BY tag_rank_score_{score_type} DESC) AS r
                , last_query_score
            FROM niconico.content.content_nicovideo_tag_algo_v1
            WHERE run_date = TO_DATE('${log_days}', 'yyyymmdd')
            QUALIFY tag_rank_score_{score_type} > 0.0
        )
    WHERE r <= 10
),
count_each_tag AS (
    SELECT tag, COUNT(DISTINCT content_id) AS count
    FROM tag_log
    GROUP BY tag
),
video_ranking_with_tag AS (
    SELECT
        video_ranking.ranking,
        tag_log.tag
        , video_ranking.content_id
    FROM video_ranking
    JOIN tag_log ON video_ranking.content_id = tag_log.content_id
),
selected_topn_tag AS (
    SELECT
        ranking,
        tag,
        content_id
    FROM (
            SELECT
                ranking,
                tag,
                content_id
                , ROW_NUMBER()
                    OVER (PARTITION BY ranking ORDER BY tag) AS r
            FROM video_ranking_with_tag
            JOIN count_each_tag ON video_ranking_with_tag.tag = count_each_tag.tag
            WHERE count > ${tag_min_videos}
        )
    WHERE r <= ${per}
)
SELECT
    ranking,
    content_nicovideo_video_v2.content_id
FROM selected_topn_tag
JOIN niconico.content.content_nicovideo_video_v2 ON selected_topn_tag.content_id = content_nicovideo_video_v2.content_id
;

```

**感想**

- なぜ watch_event に 2 回 JOIN してる？
