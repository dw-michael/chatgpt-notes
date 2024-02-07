[« 静画紹介](./07_seiga.md)

# 概要

カメラのコマンドを追加する

# 出力例

**キャラクター**：

```json
{
    "id": 0,
    "gender": "Female",
    "name": "イヌ子",
    "description": "元気いっぱいで人懐っこいな犬耳少女。テンションが上がった時に「わん！」と言う。ネコ美のことを「ネコ美ちゃん」と呼んで、ネコ美の辛辣な発言を全部ポジティブに受け取る。基本的にボケ役とMC"
}
{
    "id": 1,
    "gender": "Female",
    "name": "ネコ美",
    "description": "極度のめんどくさがり屋の毒舌猫耳少女。「な」の代わりに「にゃ」と言いがち。全体的にネガティブな性格。タメ口。イヌ子に対しては呼び捨てでいつも辛辣なツッコミを入れるが、内心構ってほしい"
}
```

**カメラ**：

```json
{"camId": 0, "description": "全体を映す正面カメラ"},
{"camId": 1, "description": "イヌ子のアップカメラ"},
{"camId": 2, "description": "ネコ美のアップカメラ"},
```

**出力**：

![](https://lohas.nicoseiga.jp/thumb/11363590i)

```json
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11363590 【アウラ、生きろ。】投稿者: ちゃなつ！"
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11363590i"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "みんな〜、今日はニコニコ静画から、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "とっても素敵なイラストを紹介するよ！わん！",
    "facialExpression": "通常",
    "facing": "camera:0"
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
    "charaId": 1,
    "text": "ふーん、どんなイラストなのかしら。期待しないでおくにゃ。",
    "facialExpression": "ジト目",
    "facing": "character:0"
  }
}
{
  "command": "Camera",
  "data": {
    "camId": 1
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "これはね、",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "「断頭台のアウラ」っていうキャラクターが描かれているの",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "普段はすごく威厳があるんだけど、今回はジャージを着てて、",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "なんだか悲しそうに涙を流しているんだよ。",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "あら、普段とは違う一面が見れるなんて、",
    "facialExpression": "悩み顔",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ちょっと興味が出てきたかも。でも、なんで涙を流してるの？",
    "facialExpression": "悩み顔",
    "facing": "camera:2"
  }
}
{
  "command": "Camera",
  "data": {
    "camId": 1
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "実はね、アウラちゃんが買い物で使いすぎちゃって、",
    "facialExpression": "目を見開く",
    "gesture": "指を指して肯定する",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "レシートや半額シールが散らばってるの。わん！",
    "facialExpression": "目を見開く",
    "gesture": "指を指して肯定する",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": " こんなに人間らしい一面があるなんて、親近感わくよね！",
    "facialExpression": "目を見開く",
    "gesture": "指を指して肯定する",
    "facing": "camera:1"
  }
}
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "へえ、意外と日常的な悩みを持ってるんだね",
    "facialExpression": "通常",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "それにジャージ姿ってのも新鮮だわ。",
    "facialExpression": "通常",
    "facing": "camera:2"
  }
}
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "そうなの！ファンにとっては、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "アウラちゃんの新しい一面を想像する楽しみがあるんだよ。わん！",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
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
    "charaId": 1,
    "text": "ちゃなつ！さんの描くアウラちゃん、本当に魅力的ね",
    "facialExpression": "苦笑い",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ちょっと見てみたくなっちゃったわ。",
    "facialExpression": "苦笑い",
    "facing": "camera:0"
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
    "charaId": 0,
    "text": "次に紹介するイラストもすごく素敵なんだから、",
    "facialExpression": "ウィンク",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "みんな楽しみにしててね！わん！",
    "facialExpression": "ウィンク",
    "facing": "camera:0"
  }
}
```

![](https://lohas.nicoseiga.jp/thumb/11363203i)

```json
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11363203 - 作品名: 奥さんにとんでもない事実を伝えたところ... - 投稿者: ぎばちゃん"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "さてさて、次に紹介するイラストはね、",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "「奥さんにとんでもない事実を伝えたところ.",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "」っていう作品なんだよ！",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ふーん、なんかドラマチックなタイトルだにゃ。",
    "facialExpression": "悩み顔",
    "facing": "character:0"
  }
}
{
  "command": "Image",
  "data": {
    "action": "show",
    "format": "web",
    "image_url": "https://lohas.nicoseiga.jp/thumb/11363203i"
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
    "charaId": 0,
    "text": "このイラスト、",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "みかんを持ってこたつに座る女性がすごく驚いてるのが印象的だよね！",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "わん！",
    "facialExpression": "通常",
    "gesture": "指を指して肯定する",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "うん、その驚きようからして、",
    "facialExpression": "ジト目",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "相当な事実を突きつけられたんだろうにゃ",
    "facialExpression": "ジト目",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "背景のセリフが気になるにゃ。",
    "facialExpression": "ジト目",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "そうそう、こたつとみかんっていうのがほっこりするけど、",
    "facialExpression": "苦笑い",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "その対比で何か大変なことが起きてるって感じがするよね！",
    "facialExpression": "苦笑い",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ジャネーの法則っていうのもタグに入ってるけど、",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "それがどう関係してるのか気になるところだにゃ。",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "ねぇねぇ、ネコ美ちゃんもこたつでみかん食べたいって思わない？",
    "facialExpression": "ウィンク",
    "gesture": "お願い！",
    "facing": "character:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "めんどくさいけど、みかんは好きだから食べたいにゃ",
    "facialExpression": "ふくれっ面",
    "facing": "character:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "でも今はこのイラストの話をしようよ。",
    "facialExpression": "ふくれっ面",
    "facing": "character:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "そうだね！みんなもこのイラスト、ぜひチェックしてみてね！",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "投稿者のぎばちゃん、素敵な作品をありがとう！",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "camera:0"
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
    "duration": 2
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "次のイラストに行く前に、ちょっと休憩してもいいかにゃ？",
    "facialExpression": "居眠り",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "もちろんだよ！ネコ美ちゃん、ちょっと一息ついて、",
    "facialExpression": "通常",
    "gesture": "約束をする時のポーズ",
    "facing": "character:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "次のイラストに備えようね！",
    "facialExpression": "通常",
    "gesture": "約束をする時のポーズ",
    "facing": "character:1"
  }
}
```

![](https://lohas.nicoseiga.jp/thumb/11363453i)

```json
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "作品ID: im11363453 | 作品名: 新作SEED映画で学ぶ、NTR | 投稿者: tk8"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "それじゃあ次に紹介するイラストは、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "im11363453【新作SEED映画で学ぶ、NTR】だよ！",
    "facialExpression": "通常",
    "facing": "camera:0"
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
    "image_url": "https://lohas.nicoseiga.jp/thumb/11363453i"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "このイラスト、すごく感情がこもっていて、",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "見る人の心をグッと掴むんだよね。金髪の男性キャラクターが、",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "なんだか切ない表情で、わん、私まで悲しくなっちゃうよ…。",
    "facialExpression": "悲しむ",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ふーん、確かにこの表情、何かを失った悲しみがにじみ出てるにゃ",
    "facialExpression": "通常",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "アニメの線画と色使いもキレイだし、目を引くのはわかるかも。",
    "facialExpression": "通常",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "そうなんだよ、ネコ美ちゃん！このイラストには「結婚したのか、",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "俺以外のヤツと.」っていう言葉が入っていて、",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "なんだかドラマがありそうで気になるよね！",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ドラマはドラマでも、ちょっと重いテーマだにゃ。でも、",
    "facialExpression": "苦笑い",
    "facing": "character:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "そういう複雑な感情を描けるのもイラストの魅力だよね。",
    "facialExpression": "苦笑い",
    "facing": "character:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "うんうん、そうだね！投稿者のtk8さん、",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "本当に素敵な作品をありがとう！みんなもぜひチェックしてみてね！",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "camera:0"
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
    "charaId": 0,
    "text": "今日はここまで！みんな、",
    "facialExpression": "ウィンク",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "一緒にイラストを楽しんでくれてありがとう！",
    "facialExpression": "ウィンク",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "次回も楽しい作品をたくさん紹介するから、また遊びに来てね！",
    "facialExpression": "ウィンク",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "ええ、めんどくさいけどまた来てあげるにゃ。じゃあね、みんな。",
    "facialExpression": "あくび",
    "facing": "camera:0"
  }
}
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
}
```
