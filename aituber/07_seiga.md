[« テロップ同時生成](./06_new_api.md)

# 概要

ニコニコ静画の人気イラストを GPT-4-vision で紹介する。

GPT-4-vision の API がまだ `response_format=JSON` に対応していないけど自然言語で JSON を要求すれば普通は返してくれる。

# 出力例

## im11360423 【「匂い」の好みは遺伝子レベル】

![](https://lohas.nicoseiga.jp/thumb/11360423i)

```json
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "今日のイラスト紹介コーナー！"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "caption",
    "text": "作品ID: im11360423 | 作品名: 「匂い」の好みは遺伝子レベル | 投稿者: じゃがいもギャング"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "みんな、こんにちは！ずんだもんだよ～。今日はね、",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ニコニコ静画で人気のイラストを紹介するのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11360423i"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "まずはこのイラスト、作品IDはim11360423、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "タイトルは「匂い」の好みは遺伝子レベルなのだ！",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "投稿者はじゃがいもギャングさんなのだよ。",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "このイラスト、",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "上のシーンでは女の子が服の匂いを嗅いでいるの。",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "なんだか不思議そうな表情してるのが可愛いのだ～。",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "そして下のシーンでは、",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "浴室でタオルを持ってる女の子がいて、",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "何かを悟ったような笑顔なのだ。",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "二つのシーンがどう繋がってるのか気になるのだ～。",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "色使いもすごく柔らかくて、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "見てるだけでほっこりするのだ。",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "日常の小さな瞬間を切り取ったようなイラストは、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "物語を想像させるのが魅力なのだね。",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "じゃがいもギャングさん、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "素敵なイラストをありがとうなのだ！",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "みんなもぜひチェックしてみてね～。",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "Image",
  "data": {
    "action": "hide",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11360423i"
  }
}
{
  "command": "Telop",
  "data": {
    "action": "hide",
    "position": "caption",
    "text": null
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "さてさて、次のイラストも楽しみなのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "どんな作品が待ってるのかな～？",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
```

## im11360499 【知識欲旺盛な教え子】

![](https://lohas.nicoseiga.jp/thumb/11360499i)

```json
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11360499 【知識欲旺盛な教え子】"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "さてさて、次に紹介するイラストはこちらなのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11360499i"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "タイトルは「知識欲旺盛な教え子」、",
    "facialExpression": "ウィンク"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "投稿者はハマーさんなのだ！",
    "facialExpression": "ウィンク"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "このイラスト、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "セーラー服を着た女の子がびっくりしてる表情がとっても印象的なのだよね～。",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "花の飾りがついた髪も、大きな瞳も、",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "すっごく可愛らしいのだ！",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "色使いが明るくて、",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "見ているだけで元気が出てくるような感じがするのだ。",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "でもね、",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "このイラストには「検索してはいけない言葉」というタグがついているのだ。",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "これはね、",
    "facialExpression": "ジト目"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ちょっと怖いものやトラウマになるようなものが関連していることがあるから、",
    "facialExpression": "ジト目"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "気をつけてね！",
    "facialExpression": "ジト目"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "でもこのイラストは、",
    "facialExpression": "通常",
    "gesture": "頑張れ！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "そんなことを忘れさせてくれるくらい、魅力的なのだ！",
    "facialExpression": "通常",
    "gesture": "頑張れ！"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ハマーさん、素敵なイラストをありがとうなのだ！",
    "facialExpression": "目をそらす",
    "gesture": "お願い！"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
{
  "command": "Telop",
  "data": {
    "action": "hide",
    "position": "title",
    "text": null
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "今日の人気イラスト紹介はここまでなのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "次のコーナーもお楽しみになのだ～！",
    "facialExpression": "ウィンク"
  }
}
```
