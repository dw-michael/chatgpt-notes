[« カメラコマンド](./08_camera.md)

# 概要

簡単なイントロ雑談。お題も指定できるが、指定しなかった場合は日常系アニメ的な何気ない会話を生成してくれる。

# 出力例

**お題指定なし**

```json
{
  "command": "Corner",
  "data": {
    "action": "start",
    "name": "イントロ"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "みんな、こんにちは～！今日も元気いっぱい、イヌ子だよ！わん！",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "はいはい、こんにちは。ネコ美だにゃ",
    "facialExpression": "ふくれっ面",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "今日もめんどくさいことに付き合わされてるにゃ。",
    "facialExpression": "ふくれっ面",
    "facing": "camera:0"
  }
},
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 1
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "ねえねえ、ネコ美ちゃん！今朝ね、お散歩してたら、",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "虹色の蝶々を見つけたの！きれいでね、",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "つい追いかけちゃったんだよ～！",
    "facialExpression": "目を見開く",
    "facing": "character:1"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "虹色の蝶々って、どんな夢見てるの？現実じゃ見たことないわよ",
    "facialExpression": "ジト目",
    "facing": "character:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "イヌ子の頭の中はいつもカラフルでうらやましいにゃ。",
    "facialExpression": "ジト目",
    "facing": "character:0"
  }
},
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 1
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "えへへ、ネコ美ちゃんも一緒に追いかけたら楽しいよ！",
    "facialExpression": "通常",
    "gesture": "お願い！",
    "facing": "character:1"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "次は一緒に行こうね！",
    "facialExpression": "通常",
    "gesture": "お願い！",
    "facing": "character:1"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "まったく、君といると退屈しないわね。でも、その、",
    "facialExpression": "苦笑い",
    "facing": "character:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "案外楽しそうかもしれないにゃ。",
    "facialExpression": "苦笑い",
    "facing": "character:0"
  }
},
{
  "command": "Pause",
  "data": {
    "duration": 2
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "それじゃあ、今日のワンニャン座談会、始めるよ～！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "今日もいっぱいお話ししようね！わん！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "はいはい、始めるわよ。今日も面倒見てあげるから、期待しててね",
    "facialExpression": "ドヤ顔",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "にゃ。",
    "facialExpression": "ドヤ顔",
    "facing": "camera:0"
  }
},
{
  "command": "Corner",
  "data": {
    "action": "end",
    "name": "イントロ"
  }
}
```

**お題：今日は寒い**

```json
{
  "command": "Corner",
  "data": {
    "action": "start",
    "name": "イントロ"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "こんにちは〜！イヌ子です！わん！今日はめっちゃ寒いね〜。みんな、",
    "facialExpression": "目を見開く",
    "gesture": "挑発ポーズ",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "暖かくしてる？",
    "facialExpression": "目を見開く",
    "gesture": "挑発ポーズ",
    "facing": "camera:0"
  }
},
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "もう、寒すぎて動くのもめんどくさいにゃ。",
    "facialExpression": "ふくれっ面",
    "gesture": "寝っ転がる",
    "facing": "camera:0"
  }
},
{
  "command": "Pause",
  "data": {
    "duration": 1
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "ネコ美ちゃん、そんなに寒いなら、",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "character:1"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "私がぬくぬくの毛布になってあげるよ！",
    "facialExpression": "通常",
    "gesture": "頑張れ！",
    "facing": "character:1"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "…ありがたいけど、それはそれでちょっと…ねぇ？",
    "facialExpression": "苦笑い",
    "facing": "character:0"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 1
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "え〜、でも一緒にいたら暖かいよ！ほら、犬って温かいって言うし！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "character:1"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "わん！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "character:1"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 2
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 1,
    "text": "そうにゃんだけどさ、今日は特別寒いから、",
    "facialExpression": "居眠り",
    "facing": "camera:0"
  }
},
{
  "command": "Camera",
  "data": {
    "camId": 0
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "そんな寒い日は、みんなで一緒に「犬猫の世界」を見て温まろうよ！",
    "facialExpression": "ウィンク",
    "gesture": "お願い！",
    "facing": "camera:0"
  }
},
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "さぁ、本編スタートだよ！",
    "facialExpression": "ウィンク",
    "gesture": "お願い！",
    "facing": "camera:0"
  }
},
{
  "command": "Corner",
  "data": {
    "action": "end",
    "name": "イントロ"
  }
}
```
