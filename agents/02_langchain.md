[« エージェンとを実装してみる](./01_test_cooking_agent.md)

# 概要

langchain ライブラリを使ってみて簡単にエージェントが作れるかを試してみる

https://github.com/hwchase17/langchain

# メモ

AutoGPT や自分が実装してみたエージェントと違って、JSON などの形式を介せずに割と自然言語っぽく出力してもらってる

しかもプロンプトがかなり短い（ほぼ出力形式を定義しているだけ）

ただしこれでしくじることもある

```
File ~/.conda/envs/michaelenv/lib/python3.9/site-packages/langchain/agents/mrkl/output_parser.py:24, in MRKLOutputParser.parse(self, text)
     22 match = re.search(regex, text, re.DOTALL)
     23 if not match:
---> 24     raise OutputParserException(f"Could not parse LLM output: `{text}`")
     25 action = match.group(1).strip()
     26 action_input = match.group(2)
```

コードを覗いてみたら、このエラーになった理由が：

```
Action: アクション名
Action Input: アクションの引数
```

を期待する正規表現を使っていたのに

```
Action: None
```

が渡されて正規表現がパースできなかったからです。

こういうことがあり得るから出力の形式を固く定義する必要がある、あるいは GPT-4 を使う必要がある。

「日本語で答えてください」と言っても英語で返ってくることはある。ライブラリ内装のプロンプトなどもやはり英語。

便利関数を使わなければプロンプトを手動で設定することもできるので日本語で設定してみた

ニコニコの検索 API を使えるようにしたけどやはりルールを破ってしまうことが多い

```
Thought: 音楽ジャンルの最新のデータを収集する必要がある
Action: ニコニコ動画検索
Action Input: { "query": "2023年4月", "targets": ["genre"], "fields": ["title", "genre"], "sort": "startTime", "sort_order": "descending" }title,genre
 検索結果を分析する必要がある
Action: データ分析
Action Input: 検索結果データ分析 is not a valid tool, try another one. 検索結果をグラフ化する
Action: データ可視化
Action Input: 検索結果データ可視化 is not a valid tool, try another one. 検索結果をレポートにまとめる
Action: レポート作成
Action Input: 検索結果レポート作成 is not a valid tool, try another one. 検索結果を解析してレポートにまとめる
Action: データ解析
Action Input: 検索結果データ解析 is not a valid tool, try another one.
etc.
```

# 成功（出力までいけた）例

LLM にわかりやすくするために、検索 API のフィールド名をいくつか変えた（API とやりとりするクラスで元に戻してる）

例えば userId -> uploaderId

## 音楽ジャンルの人気投稿者

**入力**: 「音楽」ジャンルの一番人気の投稿者を教えてください

**エージェントからの結果**: 音楽ジャンルの一番人気の投稿者は ID が 4 であることがわかりました。

**メモ**

レッツゴー！陰陽師の投稿者が ID 4

確かに一番再生数が多い一本の動画の投稿者を選んでくれたけど、全体的に一番人気の投稿者とは言いづらい

過程を見ると、上位の投稿者の他の動画も調べようとしてくれたけど、検索 API で同じ投稿者の動画を検索できなそうなので仕方なかったかもしれない：

```
 上位の投稿者を調べる
Action: ニコニコ動画検索
Action Input: { "query": "uploaderId: 16834193", "search in": ["uploaderId"], "return fields": ["title", "viewCount"], "sort by": "viewCount", "sort order": "descending" }
検索エラーが出ました：{"meta":{"errorMessage":"parameter error: 'targets'","errorCode":"QUERY_PARSE_ERROR","id":"55f4147e-e13b-474a-8985-7ad8b2f20cda","status":400}}
```

## 音楽ジャンルの傾向 ①

**入力**: 最近と昔の「音楽」ジャンルの傾向を比べてください

**エージェントからの結果**: 最近の "音楽" ジャンルの動画が多いことがわかりました。

**メモ**

過程を見てみると面白いけど呆れる

```
> Entering new AgentExecutor chain...
Thought: "genre" フィールドを使ってどのような傾向が見られるかを考える
Action: ニコニコ動画検索
Action Input: {
    "query": "音楽",
    "search in": ["genre"],
    "return fields": ["uploadTime"],
    "sort by": "uploadTime",
    "sort order": "descending"
}
uploadTime
2023-04-21T04:50:02+09:00
2023-04-21T04:47:02+09:00
2023-04-21T04:45:02+09:00
2023-04-21T04:29:02+09:00
2023-04-21T04:13:02+09:00
2023-04-21T04:04:02+09:00
2023-04-21T04:01:00+09:00
2023-04-21T03:32:02+09:00
2023-04-21T03:27:02+09:00
2023-04-21T03:06:02+09:00

 結果から最近の "音楽" ジャンルの動画が多いことがわかる
Final Answer: 最近の "音楽" ジャンルの動画が多いことがわかりました。
```

## 音楽ジャンルの傾向 ②

**入力**: 最近と昔の「音楽」ジャンルの動画の傾向を比べてください

**エージェントからの結果**: 最近の「音楽」ジャンルの動画の viewCount, commentCount が最近よりも多いことがわかりました。

**メモ**

最近のを最近のと比べてる？？？

```
> Entering new AgentExecutor chain...
Thought: contentId, viewCount, commentCount, lastCommentTimeなどの項目を比較してみる
Action: ニコニコ動画検索
Action Input: {"query": "音楽", "search in": ["genre"], "return fields": ["contentId", "viewCount", "commentCount", "lastCommentTime"], "sort by": "lastCommentTime", "sort order": "descending"}
contentId,viewCount,commentCount,lastCommentTime
sm41755374,1689,338,2023-04-21T04:59:23+09:00
sm42070239,743181,2173,2023-04-21T04:58:59+09:00
sm41843633,491,12,2023-04-21T04:56:20+09:00
sm35548406,274852,895,2023-04-21T04:55:34+09:00
sm34963216,523952,1697,2023-04-21T04:53:48+09:00
sm41736512,175,4,2023-04-21T04:50:14+09:00
so42107348,3717,14,2023-04-21T04:49:05+09:00
sm41880635,94,3,2023-04-21T04:49:02+09:00
sm24630720,13622,51,2023-04-21T04:48:39+09:00
sm34562705,2091,37,2023-04-21T04:48:36+09:00

 最近と昔の「音楽」ジャンルの動画のviewCount, commentCount, lastCommentTimeなどの項目を比較してみる
Action: ニコニコ動画検索
Action Input: {"query": "音楽", "search in": ["genre"], "return fields": ["viewCount", "commentCount", "lastCommentTime"], "sort by": "lastCommentTime", "sort order": "descending"}
viewCount,commentCount,lastCommentTime
1689,338,2023-04-21T04:59:23+09:00
743181,2173,2023-04-21T04:58:59+09:00
491,12,2023-04-21T04:56:20+09:00
274852,895,2023-04-21T04:55:34+09:00
523952,1697,2023-04-21T04:53:48+09:00
175,4,2023-04-21T04:50:14+09:00
3717,14,2023-04-21T04:49:05+09:00
94,3,2023-04-21T04:49:02+09:00
13622,51,2023-04-21T04:48:39+09:00
2091,37,2023-04-21T04:48:36+09:00

 最近と昔の「音楽」ジャンルの動画のviewCount, commentCount, lastCommentTimeなどの項目を比較したところ、最近のほうがviewCount, commentCountが多いことがわかった
Final Answer: 最近の「音楽」ジャンルの動画のviewCount, commentCountが最近よりも多いことがわかりました。
```

ソートの方向を ascending にしないで実質同じ検索を 2 回行ったねぇ…

## 音楽ジャンルの傾向 ③

**入力**: 最近と昔の「音楽」ジャンルの動画の傾向を比べてください

**エージェントからの結果**: 最近の動画のジャンルの割合は、音楽・サウンドが最も多く、他のジャンルは以下の順番において少なかった: ゲーム、アニメ、旅行・アウトドア、ラジオ、エンターテイメント。

**メモ**

質問の意図を勘違いしたようだ、言い換えた方がいい？

```
> Entering new AgentExecutor chain...
Thought: 今回はニコニコ動画検索を使用して動画を見つけて、ジャンルを比較します
Action: ニコニコ動画検索
Action Input: {
    "query": "音楽",
    "search in": ["title", "description", "tags"],
    "return fields": ["title", "uploadTime", "genre"],
    "sort by": "uploadTime",
    "sort order": "descending"
}
title,uploadTime,genre
【作業用BGM】『ファイナルファンタジーⅤ』植松伸夫氏with天野喜孝氏,2023-04-21T04:04:02+09:00,音楽・サウンド
[オリジナル] Upheaval,2023-04-21T03:00:03+09:00,音楽・サウンド
格ゲー界の伝説「ウメハラ」徹底解説！クール？変人？講演者？【ゆっくり解説】,2023-04-21T02:44:04+09:00,ゲーム
週刊VOCAL CharacterとUTAUランキング　#811・753,2023-04-21T01:20:00+09:00,音楽・サウンド
異世界でチート能力を手にした俺は、現実世界をも無双する ～レベルアップは人生を変,2023-04-21T01:00:00+09:00,アニメ
【ゲスト中田花奈】SONAR MUSIC(2023年04月18日),2023-04-21T00:50:03+09:00,ラジオ
レクイエム(kanaria)feat.星街すいせいcv歌を歌う人,2023-04-21T00:43:02+09:00,音楽・サウンド
海中の鳥居から山頂の鳥居へ【ボロボロ日本語で日本旅行2023春#04】,2023-04-21T00:39:03+09:00,旅行・アウトドア
天ノ弱/164 【Coverd by Namakemono_P】,2023-04-21T00:26:02+09:00,音楽・サウンド
ゆかりさんが愚痴を聞いてもらいたいそうです。【第三回10秒動画祭】,2023-04-21T00:20:00+09:00,エンターテイメント

 最近と昔の動画のジャンルを比較するために、検索結果から抽出したジャンルの割合を調べます。
Final Answer: 最近の動画のジャンルの割合は、音楽・サウンドが最も多く、他のジャンルは以下の順番において少なかった: ゲーム、アニメ、旅行・アウトドア、ラジオ、エンターテイメント。
```

## 英語タスク＋ Google 検索 ①

二つのテレビドラマに両方出演した役者を教えて欲しいと（正解は少なくとも一人います： Gwendoline Christie ）

**入力**: What actors appeared in both Sandman and Game of Thrones?

**エージェントからの結果**: There are no actors who appeared in both Sandman and Game of Thrones.

**メモ**

```
> Entering new AgentExecutor chain...
I should use a search engine to find the answer to this question.
Action: Search
Action Input: "actors in both Sandman and Game of Thrones"
For the full cast list, see below.
I need to look through the list to find the actors who appeared in both.
Action: Search
Action Input: "Sandman and Game of Thrones cast list"
For the full cast list, see below.
I should use the "find" function to search for specific names on the cast list.
Action: Search
Action Input: "ctrl+f and search for actor names on cast list"
When I go to a cast list of an episode / movie I would like to be able to search for the characters name.
I now know the final answer.
Final Answer: There are no actors who appeared in both Sandman and Game of Thrones.
```

多分検索結果に IMDB が一番最初に出てきて、「出演者一覧はこちらをクリックしてください」という文章だけがスクレープされてしまい有用な情報を得なかった。

## 英語タスク＋ Google 検索 ②

**入力**: What relatives of Will Smith are also actors?

**エージェントからの結果**: Will Smith's half-sister, Ashley Marie Pettway Smith, is an aspiring actress and singer.

**メモ**

```
> Entering new AgentExecutor chain...
I should use a search engine to find the answer to this question.
Action: Search
Action Input: "Will Smith actor relatives"
Willard Carroll Smith II is an American actor and rapper. He has received multiple accolades, including an Academy Award, a British Academy Film Award and four Grammy Awards. As of 2023, his films have grossed over $9.3 billion globally, making him one of Hollywood's most bankable stars.
That's not the answer to my question. I need to refine my search.
Action: Search
Action Input: "Will Smith actor family members"
Willard Carroll Smith II is an American actor and rapper. He has received multiple accolades, including an Academy Award, a British Academy Film Award and four Grammy Awards. As of 2023, his films have grossed over $9.3 billion globally, making him one of Hollywood's most bankable stars.
That's still not the answer I'm looking for. I need to be more specific.
Action: Search
Action Input: "Will Smith actor siblings"
Willard Carroll Smith II is an American actor and rapper. He has received multiple accolades, including an Academy Award, a British Academy Film Award and four Grammy Awards. As of 2023, his films have grossed over $9.3 billion globally, making him one of Hollywood's most bankable stars.
This search isn't giving me the information I need. I should try a different approach.
Action: Search
Action Input: "Which of Will Smith's siblings are actors?"
Will has a half-sister, Ashley Marie Pettway Smith, who is an aspiring actress and singer.
That's the answer I was looking for!
Final Answer: Will Smith's half-sister, Ashley Marie Pettway Smith, is an aspiring actress and singer.

> Finished chain.
```

答えにはなっているけど、息子も娘も妻も俳優の経験があるのでそれらをピックアップして欲しかった

使っている検索 API の限界も少し感じる（最初の結果の文章だけを返している？）。設定できると思うけどこのライブラリのドキュメントを読むと設定の仕方がわからない

いろんな実験を通しての感想は：

- 一つの検索で全部済ませたがる
  - まずはウィル・スミスの家族を調べて、一人ずつ俳優かどうかを調べるという選択肢もあったはず
  - 「タスクを分解して段階を踏んで考えてください」みたいな指示をしてもなりうる
- やっぱり同じことを、失敗しても繰り返しがち
  - 「失敗したらやり方を変えてください」みたいな指示をしてもやっぱりなりうる

## 英語タスク＋ Google 検索 ③

**入力**: Create a playlist of three songs: one from the 70s, one from the 80s, and one from the 90s, each one representing the most popular genre of their decade. Try breaking up your searches to look for only one piece of information at a time. Don't include brackets in your action selection.

**エージェントからの結果**: "Stayin' Alive" by the Bee Gees, "Master Blaster (Jammin')" by Stevie Wonder, and "The World Is Yours" by Nas.

**メモ**

今までの一番の成功例！入力をかなり工夫する必要があったけど、今回はちゃんと指示通りに検索を一つずつして、最後にその情報を組み合わせて答えを出してくれた

指示しないと、ずっと一個の検索で済ませようとして失敗してしまうことを確認できた。そもそもこの LLM は検索の上手い使い方をあまり知らない気がする

```
> Entering new AgentExecutor chain...
I should start by searching for the most popular genres of each decade.
Action: Search
Action Input: "most popular music genres of the 70s"
Popular Music from the 1970s, Genres including Disco/Club, Progressive Rock, Punk Rock/New Wave, Funk & Soul and top songs and artists from each year.
Great, now I can search for the most popular songs in each genre.
Action: Search
Action Input: "most popular disco songs of the 70s"
7 of the Best Disco Songs of the '70s · 1. “Stayin' Alive” by the Bee Gees (1977) · 2. “I Will Survive” by Gloria Gaynor (1978) · 3. “Dancing Queen ...
Now I need to search for the most popular genres of the 80s.
Action: Search
Action Input: "most popular music genres of the 80s"
Throughout the decade, R&B, hip hop, and urban genres were becoming commonplace, particularly in the inner-city areas of large, metropolitan cities; rap was ...
Okay, time to search for the most popular songs in the R&B/hip hop genre of the 80s.
Action: Search
Action Input: "most popular R&B/hip hop songs of the 80s"
According to Billboard, the top 3 Songs for 1980 were: Celebration by Kool & The Gang, Love T.K.O. by Teddy Pendergrass, and Master Blaster (Jammin') by Stevie ...
Now I need to search for the most popular genres of the 90s.
Action: Search
Action Input: "most popular music genres of the 90s"
The most popular style of music in the '90s was hip-hop, closely followed by rap and contemporary R&B. Hip-hop redefined the Billboard charts in ...
Last search, I need to find the most popular songs in the hip-hop genre of the 90s.
Action: Search
Action Input: "most popular hip-hop songs of the 90s"
No good search result found
I'll try searching for "top hip hop songs of the 90s" instead.
Action: Search
Action Input: "top hip hop songs of the 90s"
1. “The World Is Yours” by Nas. “The World Is Yours” is taken from Nas' debut ...
Great, I now have my three songs: "Stayin' Alive" by the Bee Gees for the 70s disco genre, "Master Blaster (Jammin')" by Stevie Wonder for the 80s R&B/hip hop genre, and "The World Is Yours" by Nas for the 90s hip hop genre.
Final Answer: "Stayin' Alive" by the Bee Gees, "Master Blaster (Jammin')" by Stevie Wonder, and "The World Is Yours" by Nas.
```
