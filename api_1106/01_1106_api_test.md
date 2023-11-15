# 概要

11 月 6 日に導入された新しい API 仕様を触ってみて感覚を掴む：

- GPT-4-turbo プレビュー、GPT-3.5-turbo-1106 がリリース
- 関数 → ツール：関数の上のさらなる抽象化、複数呼び出しにも対応
- response_format: json_object が導入

# 使ってみた感想

## ツール

- 今までは正しい JSON 形式を返してもらうためだけに関数を使っていたが、本来は外部 API の呼び出しなどに使うのが正しい使い方みたい
- 例）複雑な計算を計算機に解いてもらって、その結果を LLM に返す
- ツールを使う場合は、それぞれのツール呼び出しに「結果」を返さないといけないみたい（じゃないと API エラーが出て、「このツール呼び出し ID に対応する返事がないよ」と怒られる）
- 今までみたいに使おうとすると何故か不安定？今まで使えた関数定義をツールにしただけで、大量の改行が生成され JSON が崩れてパースできなかった
- 単に JSON 形式の返信が欲しい場合は…

## response_format: json_object

- ただ JSON の返事が欲しい場合はこれを使うべきみたい
- 関数と違って、jsonschema で固く定義しなくてもよくて、自然言語寄りの定義をしてもちゃんと形式を守ってくれる
- jsonschema で定義しにくい、または定義できない形式も定義できて、それに従って返信してくれる

### 例

```
【システムメッセージ】
あなたはエンタテインメント番組の台本を書く台本家。「台本」は任意のアクションの列である。

返信の形式は以下の通りのJSON:
{
    "script": [
        CHARACTER_ACTION,
        CHARACTER_ACTION,
        TELOP_ACTION,
        CHARACTER_ACTION,
        ...
    ]
}

CHARACTER_ACTION:
{
    "type": "character",
    "character_id": 数字、喋っているキャラクターのID,
    "message": 文字列、キャラクターのセリフ,
    "expression": 文字列、次のうちのどれか： ["neutral", "happy", "sad", "angry", "surprised"]
}

TELOP_ACTION:
{
    "type": "telop",
    "action": 文字列、次のうちのどれか： ["show", "hide"] テロップが要らなくなった時の「hide」アクションを忘れずに,
    "position": 文字列、次のうちのどれか： ["main_title", "caption"],
    "message": 文字列、テロップで表示する文章、hideの場合はnull
}

登場人物：

キャラクター0：犬山ワンコ、元気いっぱいでちょっとおバカな犬耳少女
キャラクター1：猫又くろみ、毒舌で闇深い猫耳少女


【ユーザーメッセージ】
架空なニュース番組の台本を書いてください。二人のキャラクターは番組のアナウンサー。

二人は架空な街に起こった盗難事件について報道している。事件の詳細を創作してよい。事件の紹介が終わるまでの台本を書いてください。

番組の始まりでメインタイトルを表示して、イントロが終わってニュースの紹介に移るタイミングで非表示にしてください。

それぞれのニュースに合わせたキャプションを表示して、そのニュースの紹介が終わったら非表示にしてください。
```

**返信：**

```json
{
  "script": [
    {
      "type": "telop",
      "action": "show",
      "position": "main_title",
      "message": "にゃんわんニュースライブ"
    },
    {
      "type": "character",
      "character_id": 0,
      "message": "みなさんこんばんワン！にゃんわんニュースライブ、今夜も始まります！",
      "expression": "happy"
    },
    {
      "type": "character",
      "character_id": 1,
      "message": "今宵も闇のニュースをお届けするわ。ふっ、ありふれた平和な夜だと思ったら大間違いよ。",
      "expression": "neutral"
    },
    {
      "type": "telop",
      "action": "hide",
      "position": "main_title",
      "message": null
    },
    {
      "type": "telop",
      "action": "show",
      "position": "caption",
      "message": "特報：幻想街で起きた驚きの盗難事件"
    },
    {
      "type": "character",
      "character_id": 0,
      "message": "それでは最初のニュースです！幻想街で、なんと巨大な金の像が盗まれる事件があったんですって！",
      "expression": "surprised"
    },
    {
      "type": "character",
      "character_id": 1,
      "message": "そう、その像は街のシンボルとも言える「黄金のワンコ像」。朝にはそこにあったものが、いつの間にか姿を消していたの。",
      "expression": "sad"
    },
    {
      "type": "character",
      "character_id": 0,
      "message": "えー！大きなワンコ像がどうしていなくなっちゃうんですか？それはもう、大事件ですよね！",
      "expression": "surprised"
    },
    {
      "type": "character",
      "character_id": 1,
      "message": "目撃者によると、夜中に謎の人影が像の周りをうろついていたとか。警察は盗難団の仕業ではないかと見ているわ。",
      "expression": "neutral"
    },
    {
      "type": "character",
      "character_id": 0,
      "message": "おおー、怖いですねぇ！でも、あんな大きな像をどうやって運ぶんでしょうか？",
      "expression": "surprised"
    },
    {
      "type": "character",
      "character_id": 1,
      "message": "それが問題ね。像の重さは約2トン、普通の手段ではとてもじゃないけど運べないわ。警察も頭を悩ませているみたい。",
      "expression": "sad"
    },
    {
      "type": "character",
      "character_id": 0,
      "message": "うーん、謎が謎を呼ぶ事件ですね！早く解決するといいですけど。",
      "expression": "sad"
    },
    {
      "type": "character",
      "character_id": 1,
      "message": "この事件に関する最新の情報が入り次第、また報告するわ。金のワンコ像、無事に見つかるといいのだけれど。",
      "expression": "neutral"
    },
    {
      "type": "telop",
      "action": "hide",
      "position": "caption",
      "message": null
    }
  ]
}
```

jsonschema で定義しにくい（もしかしたら定義できない？）混ざったオブジェクトの列をちゃんと返してくれて、指示通りのタイミングでテロップも生成してくれる。
