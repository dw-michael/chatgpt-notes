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

キャラ名と作品がタグにあるのになぜか今回ピックアップされなかった（情報は渡しているしタグも大百科の記事も要約してもらい最終段階の出力に渡している）

一応 Trinity クエリでは R-18 やアダルトスコアの高いものを弾いているが、これはちょっと際どい。LLM でタグなどで弾いてもらうといいかも？

さらに、GPT-4-vision の説明にも書いてある通り、画像にある英語以外の文字は基本的に検知されない。ニコニコ静画の人気イラストには漫画やセリフの入ったイラストが多いので、その内容を理解できないのは残念。

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

## im11362020 【ウマ娘】親友の子供【シーザリオ】

![](https://lohas.nicoseiga.jp/thumb/11362020i)

```json
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "【ウマ娘】親友の子供【シーザリオ】"
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "caption",
    "text": "作品ID: im11362020 | 投稿者: 坂崎ふれでぃ■(土)東ラ01ab"
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
    "text": "ニコニコ静画で大人気のイラストを紹介するのだ！",
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
    "text": "まずはこの「【ウマ娘】親友の子供【シーザリオ】」っていう作品なのだ！",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "投稿者は坂崎ふれでぃ■さんなのだよ。",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "とっても素敵な4コマ漫画なのだ！",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11362020i"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "このイラストはね、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "シーザリオちゃんが新聞を読んでいて、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "アドマイヤグルーヴちゃんが話しかけるところから始まるのだ。",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ドゥラメンテちゃんも加わって、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "3人で楽しそうにしているのがとってもキュートなのだ～。",
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
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "最後のコマでね、",
    "facialExpression": "ドヤ顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "シーザリオちゃんが「親友の子供」って見出しにドキッとするところが、",
    "facialExpression": "ドヤ顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "なんとも言えず面白いのだ！",
    "facialExpression": "ドヤ顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ウマ娘たちの日常が垣間見えて、",
    "facialExpression": "ドヤ顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ファンにはたまらないよね～。",
    "facialExpression": "ドヤ顔"
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
    "text": "キャラクターたちの表情や仕草がとっても魅力的で、",
    "facialExpression": "通常",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "見ているだけで楽しくなっちゃうのだ！",
    "facialExpression": "通常",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "坂崎ふれでぃ■さん、",
    "facialExpression": "通常",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "素敵なイラストをありがとうなのだ！",
    "facialExpression": "通常",
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
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "さてさて、次に紹介するイラストも楽しみにしていてね！",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ずんだもんはまだまだお話しすることがいっぱいあるのだ！",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
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
  "command": "Telop",
  "data": {
    "action": "hide",
    "position": "caption",
    "text": null
  }
}
```

説明が色々と間違ってるしやはり漫画は難しいかも

## im11361875【クギを刺す奥さん】

![](https://lohas.nicoseiga.jp/thumb/11361875i)

```json

{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11361875【クギを刺す奥さん】"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "さてさて、次に紹介するイラストはね、",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "「クギを刺す奥さん」っていう作品なのだ！",
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
    "text": "このイラスト、",
    "facialExpression": "ウィンク"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ぎばちゃんっていう素敵な作家さんが描いたのだよ。",
    "facialExpression": "ウィンク"
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11361875i"
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
    "text": "見て見て、この振り返りながら微笑む女性、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "なんだかこちらまで幸せな気持ちになっちゃうよね。",
    "facialExpression": "目を見開く"
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
    "text": "黒いワンピースがとってもおしゃれで、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "金髪の髪型も素敵なのだ。",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
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
    "text": "そしてね、このイラストの線の細かさや陰影の使い方が、",
    "facialExpression": "ドヤ顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "もう本当にリアルで立体感があるのだよ。",
    "facialExpression": "ドヤ顔"
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
    "text": "ぎばちゃんの他の作品も見てみたいな～。あ、",
    "facialExpression": "目をそらす"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ちなみにぎばちゃんの小説版「ボロボロのエルフさんを幸せにする薬売りさん」も大好評だって！",
    "facialExpression": "目をそらす"
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
    "text": "この「クギを刺す奥さん」、",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "なんだか物語がありそうでワクワクするよね。",
    "facialExpression": "悩み顔"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "奥さんの表情から色々と想像が膨らむのだ。",
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
    "text": "それじゃあ、次のイラストに行く前に、",
    "facialExpression": "通常",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "もう一度ぎばちゃんの「クギを刺す奥さん」を堪能してほしいなのだ！",
    "facialExpression": "通常",
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
  "command": "Pause",
  "data": {
    "duration": 1
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "次に紹介するイラストもすごく楽しみなのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "どんな作品が待っているかな～？",
    "facialExpression": "通常"
  }
}
```

## im11361924 【猫カフェ】

![](https://lohas.nicoseiga.jp/thumb/11361924i)

```json

{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11361924 【猫カフェ】"
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
    "text": "それじゃあ次に紹介するのは、",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "砲鐵さんが投稿された「猫カフェ」っていうイラストなのだ！",
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
    "text": "このイラストはね、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ウマ娘プリティーダービーのマンハッタンカフェちゃんが、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "猫耳と尻尾をつけてるんだよ～。もう、",
    "facialExpression": "目を見開く"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "めちゃくちゃ可愛いのだ！",
    "facialExpression": "目を見開く"
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
    "text": "彼女、いつもはちょっと影が薄いけど、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "このイラストではね、目を閉じて頬を赤らめて、",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "すっごく幸せそうなのだ！",
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン"
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
    "text": "和風の雰囲気がある背景に、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "黒猫のシルエットがいっぱいで、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "なんだかほっこりするよね～。",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "マンハッタンカフェちゃんの「お友だち」がいるみたいで、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "物語がある感じがして素敵なのだ！",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する"
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
    "image_url": "https://lohas.nicoseiga.jp/thumb/11361924i"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 3
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "砲鐵さん、",
    "facialExpression": "目をそらす",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "こんなに素敵なイラストを描いてくれてありがとうなのだ！",
    "facialExpression": "目をそらす",
    "gesture": "お願い！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "ファンのみんなも、ぜひチェックしてみてね！",
    "facialExpression": "目をそらす",
    "gesture": "お願い！"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 1
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
    "text": "それでは、今日の人気イラスト紹介はここまでなのだ！",
    "facialExpression": "通常"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "みんな、楽しんでくれたかな？",
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
    "text": "これからもいっぱい素敵なイラストが投稿されるといいな～。",
    "facialExpression": "ドヤ顔",
    "gesture": "頑張れ！"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ずんだもん",
    "text": "また次回もお楽しみになのだ！",
    "facialExpression": "ドヤ顔",
    "gesture": "頑張れ！"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}

```
