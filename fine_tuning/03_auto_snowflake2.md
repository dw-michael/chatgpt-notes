[« 自動 Snowflake 改善](./02_auto_snowflake.md)

# 全体的感想

Fine-tuning なし

- 今までの実験と同じような問題：
- dt などのフォーマット、プロンプトで教えても間違える
- 不要な中間テーブル
- JOIN が正しくない（カラムが違ったりロジックがそもそも間違っている）

Fine-tuning あり

- よくあるフォーマットは大体守ってくれる
- 書き方（大文字小文字、改行の仕方など）が学習データに似ている
- ただ一番の問題点は**妄想しがち**、気持ち的に fine-tuning なしよりもひどい？存在しないテーブルや関数を勝手にあるものとして書いてしまったり、本題から脱線してしまったりする
- なしより形式を守ってくれるけど、完璧ではない（関数対応になったら解決するかと）

# Fine-tuning 実験１結果

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

### Fine-tuning なし（関数なし）※

※レスポンス形式を守らなかった

```sql
-- Step 1: Select the relevant tables
SELECT
  v.upload_datetime,
  t1.regular_tag AS parent_tag,
  t2.regular_tag AS child_tag,
  COUNT(*) AS cooccurrence_count
FROM niconico.content.content_nicovideo_video_v2 v
JOIN niconico.content.content_nicovideo_tag_v1 t1
  ON v.content_id = t1.content_id
JOIN niconico.content.content_nicovideo_tag_v1 t2
  ON v.content_id <> t2.content_id
-- Step 3: Filter videos uploaded after a specified datetime
WHERE v.upload_datetime > '2023-01-01'
-- Step 4: Exclude specific tags
  AND t1.regular_tag NOT IN ('タグ編集ハデキマセン',
                             '投稿者コメント',
                             'ニコニ・コモンズ',
                             '＠BGM推奨',
                             'ニコニコムービーメーカー')
  AND t2.regular_tag NOT IN ('タグ編集ハデキマセン',
                             '投稿者コメント',
                             'ニコニ・コモンズ',
                             '＠BGM推奨',
                             'ニコニコムービーメーカー')
GROUP BY v.upload_datetime, t1.regular_tag, t2.regular_tag
-- Step 7: Calculate the relevance using Simpson's coefficient
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY v.upload_datetime
  ORDER BY (2 * cooccurrence_count) / (COUNT(*) + 1) DESC
) = 1
-- Step 8: Format the result
SELECT parent_tag || ' - ' || child_tag AS related_tag_pair
FROM (
  -- Include the query above as a subquery to reuse the calculation for Simpson's coefficient
  <INSERT QUERY HERE>
)
```

こういう説明もついていた：

```
Note:
- Replace `<INSERT QUERY HERE>` in the outer query with the inner query.
- The format of the upload datetime is assumed to be 'YYYY-MM-DD' in this example. Make sure to adjust it according to the actual format used in the database.
```

**感想**

- upload_datetime の形式が違う（与えられたドキュメントには記されている）
- 最初の JOIN が間違ってる（正解： v.content_id = t2.content_id AND t1.content_id <> t2.content_id）
- GROUP BY も違う（upload_datetime が入ってるので同じ動画でグループしてしまい共起をちゃんと数えない）
- QUALIFY は使えそうではあるが upload_datetime で PARTITION するのも違う

### Fine-tuning なし（関数あり）

```sql
WITH
  -- Filter videos based on upload datetime
  filtered_videos AS (
    SELECT
      content_id
    FROM
      niconico.content.content_nicovideo_video_v2
    WHERE
      upload_datetime >= '2023-01-01'
  ),
  -- Exclude irrelevant tags
  excluded_tags AS (
    SELECT
      content_id,
      regular_tag
    FROM
      niconico.content.content_nicovideo_tag_v1
    WHERE
      regular_tag NOT IN (
        'タグ編集ハデキマセン',
        '投稿者コメント',
        'ニコニ・コモンズ',
        '＠BGM推奨',
        'ニコニコムービーメーカー'
      )
  ),
  -- Count tag pairs
  tag_pair_counts AS (
    SELECT
      a.regular_tag AS tag1,
      b.regular_tag AS tag2,
      COUNT(*) AS count
    FROM
      excluded_tags a
      JOIN excluded_tags b ON a.content_id = b.content_id AND a.regular_tag < b.regular_tag
      JOIN filtered_videos v ON a.content_id = v.content_id
    GROUP BY
      a.regular_tag,
      b.regular_tag
  ),
  -- Calculate Simpson coefficients
  sim_coefficients AS (
    SELECT
      tag1,
      tag2,
      2 * count / (SELECT COUNT(*) FROM excluded_tags) AS coefficient
    FROM
      tag_pair_counts
  )
-- Select the tag pair with the highest coefficient
SELECT
  tag1 AS child_tag,
  tag2 AS parent_tag
FROM
  sim_coefficients
ORDER BY
  coefficient DESC
LIMIT
  1;
```

**感想**

- 同じく upload_datetime の形式が違う
- `a.regular_tag < b.regular_tag` はどういうこと？（それ以外の JOIN は一応大丈夫そう）
- タグテーブル全体から SELECT しているのが良くない
- simpson の分母がタグの総数になってない？
- LIMIT 1 は間違っているけど、これはプロンプトのせい（GPT が生成した擬似ユーザー入力の誤り）

### Fine-tuning あり（関数未対応）

```sql
-- このクエリはニコニコ動画のタグ情報から関連性の高いタグのペアを抽出するためのものです。
-- タグ情報は投稿日時が指定された日時以降の動画のものを参照します。
-- このクエリは以下のステップで動作します。
--  1. content_nicovideo_video_v2 テーブルから投稿日時が指定された日時以降の動画の content_id を取得
--  2. content_nicovideo_tag_v1 テーブルから正規化されたタグの情報を取得
--  3. 1. と 2. の結果を結合して、各動画に付けられたタグの集合を作成
--  4. 各タグの出現回数をカウント
--  5. タグの共起関係を計算して、関連性の高いタグのペアを抽出
--  6. 最も関連性の高いタグのペアを表示する

WITH video_ids AS (
  SELECT
    content_id
  FROM
    niconico.content.content_nicovideo_video_v2
  WHERE
    TO_TIMESTAMP(upload_datetime) >= TO_TIMESTAMP('${start_datetime}')  -- ここで指定された日時以降の動画を対象にする
    AND upload_datetime < '${end_datetime}'
),
tag_items AS (
  SELECT
    content_nicovideo_tag_v1.content_id AS content_id,
    content_nicovideo_tag_v1.regular_tag AS tag
  FROM
   niconico.content.content_nicovideo_tag_v1
   INNER JOIN video_ids ON content_nicovideo_tag_v1.content_id = video_ids.content_id
  WHERE
   content_nicovideo_tag_v1.regular_tag <> 'タグ編集ハデキマセン'  -- 正規化に失敗したタグは除外
   AND
   content_nicovideo_tag_v1.regular_tag <> '投稿者コメント'  -- 動画に含まれるタグとは限らない
   AND
   content_nicovideo_tag_v1.regular_tag <> 'ニコニ・コモンズ'  -- 動画に含まれるタグとは限らない
   AND
   content_nicovideo_tag_v1.regular_tag <> '＠BGM推奨'  -- 動画に含まれるタグとは限らない
   AND
   content_nicovideo_tag_v1.regular_tag <> 'ニコニコムービーメーカー'  -- 動画に含まれるタグとは限らない
   AND
   content_nicovideo_tag_v1.regular_tag <> ALL (  -- 高速化のために少し冗長に書いている
    SELECT array_agg(recommend_tag) AS common_tag_list
    FROM niconico.common.tag_suggest_service_aggregated_new
    WHERE content_id = content_nicovideo_tag_v1.content_id
   )
),
tag_count AS (
  SELECT
    tag,
    COUNT(DISTINCT content_id) AS cnt  -- タグごとにスコープを制限している
  FROM tag_items
  GROUP BY tag
),
tag_join AS (
  SELECT
    tag_items.content_id AS content_id,
    tag_items.tag AS tag  -- content_id ごとのタグの列に展開したもの
  FROM tag_items
  INNER JOIN niconico.CAS.niconico_video_info_db_tag_nlp_ver2 t ON ARRAY_CONTAINS(t.ner_tags, tag_items.tag)
  WHERE t.content_id = tag_items.content_id)
SELECT
  tag,
  COUNT(DISTINCT content_id) AS cnt
FROM
  tag_count
  INNER JOIN tag_join ON tag_count.tag = tag_join.tag
GROUP BY tag
;
```

**感想**

- 存在しないテーブルを複数使っている時点で大きく問題がある（学習データにもないしどういうこと？！）
- 何がしたい？他の出力も十分問題あったが、こっちはタグの共起を数える気すらない

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

### Fine-tuning なし（関数なし）

レスポンス形式を守らなかった上に答えすら出してない

### Fine-tuning なし（関数あり）

```sql
WITH
  -- Get the tags and count the occurrences per content_id
  tag_count AS (
    SELECT
      c.content_id,
      t.regular_tag,
      COUNT(*) AS count
    FROM
      niconico.common_action.common_action_watch_event_v3 c
    JOIN
      niconico.content.content_nicovideo_tag_v1 t
    ON
      c.content_id = t.content_id
    WHERE
      c.dt BETWEEN '2023-01-01' AND '2023-01-31'
      AND c.event_type = 'start'
      AND c.content_type = 'video'
    GROUP BY
      c.content_id,
      t.regular_tag
  ),
  -- Get the pairs of tags that occur together
  tag_pairs AS (
    SELECT
      t1.regular_tag AS tag1,
      t2.regular_tag AS tag2,
      COUNT(*) AS co_occurrence_count
    FROM
      tag_count t1
    JOIN
      tag_count t2
    ON
      t1.content_id = t2.content_id
      AND t1.regular_tag < t2.regular_tag
    GROUP BY
      t1.regular_tag,
      t2.regular_tag
  )

-- Filter and sort the tag pairs based on the specified criteria
SELECT
  tag1,
  tag2,
  co_occurrence_count
FROM
  tag_pairs
WHERE
  co_occurrence_count >= 10
  AND (co_occurrence_count*1.0)/(tag_count[tag1] + tag_count[tag2]) >= 0.5
ORDER BY
  co_occurrence_count ASC
LIMIT 1;
```

**感想**

- LIMIT 1 は間違っているけど、これはプロンプトのせい（GPT が生成した擬似ユーザー入力の誤り）

### Fine-tuning あり（関数未対応）

```sql
with
    tag as (
        select distinct content_id, regular_tag
        from
            content.content_nicovideo_tag_v1
        inner join
            common_action.common_action_watch_event_v3 on
                common_action.common_action_watch_event_v3.content_id = content.content_nicovideo_tag_v1.content_id
                and event_type = 'start'
                and dt between to_char(dateadd(DAY, -7, current_timestamp()), 'YYYYMMDD') and to_char(dateadd(DAY, 0, current_timestamp()), 'YYYYMMDD')
    ),
    tag_pair as (
        select
            t1.content_id as content_id,
            t1.regular_tag as tag1,
            t2.regular_tag as tag2
        from tag as t1
        inner join tag as t2 on t1.content_id = t2.content_id
        and t1.regular_tag != t2.regular_tag
    ),
    tag_pair_count as (
        select tag1, tag2, count(*) as c from tag_pair group by tag1, tag2
    ),
    tag_pair_filtered as (
        select
            tag1,
            tag2
        from tag_pair_count
        where c >= 100 and c > 3 * (
            select count(distinct content_id) from tag_pair where tag1 = tag_pair.regular_tag
        )
    )
select
    tag1
    || '\t'
    || tag2
    || '\t'
    || c
    || '\t'
    || (
        select count(*) from tag where content_id = tag_pair_filtered.tag1
    ) as result
from tag_pair_filtered
inner join (
    select regular_tag from
        (
            select
                regular_tag,
                row_number() over (partition by tag1 order by c desc, regular_tag) as row_num
            from tag_pair_filtered
            inner join tag on tag.content_id = tag1
        )
    where row_num <= 10
) on regular_tag = tag2;
```

**感想**

- dt と event_type の扱いがちゃんとしてる
- ペアのジョインもちゃんとしてる
- カウントの閾値はどこからきている？なんの計算？
- 最後もよくわからない
