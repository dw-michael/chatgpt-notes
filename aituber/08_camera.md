[« 静画紹介](./07_seiga.md)

# 概要

カメラのコマンドを追加する

# 出力例

**カメラ**：

```json
{"camId": 0, "description": "全体を映す正面カメラ"},
{"camId": 1, "description": "イヌ子のアップカメラ"},
{"camId": 2, "description": "ネコ美のアップカメラ"},
```

**出力**：

```json
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "title",
    "text": "フィクション討論会"
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
    "characterName": "イヌ子",
    "text": "みんなー、こんにちは！イヌ子だよ！今日はね、",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "とってもワクワクするコーナー「フィクション討論会」をお届けするよ！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "わん！",
    "facialExpression": "目を見開く",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "はいはい、ネコ美だにゃ",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "今日の討論会はちょっと変わった世界観で行うから、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "視聴者のみんなも楽しんでくれたらいいにゃ。",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "caption",
    "text": "設定：人間と動物が言葉を通じてコミュニケーションを取れる世界"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "この世界ではね、動物たちも人間みたいに仕事をしたり、",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "学校に行ったりするんだって！すごいよね！",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "caption",
    "text": "お題：動物が人間のファッションアイテムを身につける文化"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "で、",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "問題は動物が人間のファッションアイテムを身につけるのが流行ってることだにゃ",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "これって動物の個性を尊重する素敵な文化なのか、",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "それとも行き過ぎた人間化なのかって話にゃ。",
    "facialExpression": "悩み顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "うーんとね、イヌ子は個性を尊重する素敵な文化だと思うよ！だって、",
    "facialExpression": "ドヤ顔",
    "gesture": "指を指して肯定する",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "帽子もサングラスも、自分を表現する素敵な手段だもん！わん！",
    "facialExpression": "ドヤ顔",
    "gesture": "指を指して肯定する",
    "facing": "camera:0"
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
    "characterName": "ネコ美",
    "text": "まぁ、それも一理あるけど、動物が人間みたいになりすぎると、",
    "facialExpression": "苦笑い",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "本来の動物らしさが失われるっていう問題もあるにゃ",
    "facialExpression": "苦笑い",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "自然の姿っていうのも、大事だと思うんだけど…。",
    "facialExpression": "苦笑い",
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
    "characterName": "イヌ子",
    "text": "でもね、ネコ美ちゃん、自然の姿って言っても、",
    "facialExpression": "ウィンク",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "私たちもVTuberとしてアバターを使ってるよね？それって、",
    "facialExpression": "ウィンク",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "ある意味ファッションと同じじゃない？わん！",
    "facialExpression": "ウィンク",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
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
    "characterName": "ネコ美",
    "text": "…それを言っちゃおしまいにゃ。でも、まぁ、",
    "facialExpression": "ふくれっ面",
    "facing": "character:イヌ子"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "確かに自分を表現する方法の一つとしてはアリかもしれないにゃ。",
    "facialExpression": "ふくれっ面",
    "facing": "character:イヌ子"
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
  "command": "Camera",
  "data": {
    "camId": 0
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "そうだよね！みんなが自分らしくいられるのが一番だもんね！",
    "facialExpression": "通常",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "それじゃあ、このお題は、個性を尊重する素敵な文化ということで、",
    "facialExpression": "通常",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "賛成派の勝ち！わんわん！",
    "facialExpression": "通常",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "仕方ないにゃ、今回はイヌ子の言う通りにしてあげる",
    "facialExpression": "ジト目",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "でも次は負けないからね、覚悟しておいてにゃ。",
    "facialExpression": "ジト目",
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
    "text": "フィクション討論会"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "さてさて、次に進む前に設定をおさらいしようかな！",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "未来都市でロボットがいっぱいで、",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "みんな趣味や好みを持ってるんだって！",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "ロボット専用の遊び場もあるんだよ！",
    "facialExpression": "目を見開く",
    "facing": "camera:0"
  }
}
{
  "command": "Telop",
  "data": {
    "action": "show",
    "position": "caption",
    "text": "【お題】ロボットが人間用遊園地で遊ぶブーム"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "で、今流行ってるのが、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "そんなロボットたちが人間のための遊園地で遊ぶことにゃ。これって、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ロボットが社会に溶け込むいい現象なのか、",
    "facialExpression": "通常",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "それともロボットに合った環境を作るべきなのか、って話にゃ。",
    "facialExpression": "通常",
    "facing": "camera:0"
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
    "characterName": "イヌ子",
    "text": "私は賛成派だよ！ロボットも遊園地で楽しんでる姿を見ると、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:1"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "なんだか仲間みたいで嬉しいなって思うもん！わん！",
    "gesture": "喜んだ時のブイサイン",
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
    "characterName": "ネコ美",
    "text": "そうかもしれないけど、ロボット専用の施設があるんだから、",
    "facialExpression": "悩み顔",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "そっちで遊ぶべきにゃ。人間の遊園地は人間用に作られてるんだから、",
    "facialExpression": "悩み顔",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ロボットには合わないかもしれないし。",
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
    "characterName": "イヌ子",
    "text": "でもね、ネコ美ちゃん、ロボットが人間の遊園地で遊んでると、",
    "facialExpression": "目を見開く",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "人間との交流も増えるし、お互いの理解も深まると思うんだ！",
    "facialExpression": "目を見開く",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "みんなでわいわい楽しむのって素敵じゃない？",
    "facialExpression": "目を見開く",
    "gesture": "頑張れ！",
    "facing": "character:ネコ美"
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
    "characterName": "ネコ美",
    "text": "うーん、それも一理あるけど、結局ロボットが遊園地で遊んでも、",
    "facialExpression": "ジト目",
    "facing": "character:イヌ子"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "感情があるわけじゃないんだから、楽しいとか感じないんじゃないの？",
    "facialExpression": "ジト目",
    "facing": "character:イヌ子"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ただのプログラムで動いてるだけにゃ。",
    "facialExpression": "ジト目",
    "facing": "character:イヌ子"
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
    "characterName": "イヌ子",
    "text": "あはは、ネコ美ちゃんったら、そんなこと言っちゃダメだよ！",
    "facialExpression": "ウィンク",
    "gesture": "お嬢様笑い",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "ロボットだって感情を持ってるかもしれないし、",
    "facialExpression": "ウィンク",
    "gesture": "お嬢様笑い",
    "facing": "character:ネコ美"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "遊園地での経験がプログラムをアップデートするきっかけになるかも！",
    "facialExpression": "ウィンク",
    "gesture": "お嬢様笑い",
    "facing": "character:ネコ美"
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
    "characterName": "ネコ美",
    "text": "まあ、それもそうかもしれないけど……実は私、",
    "facialExpression": "苦笑い",
    "facing": "camera:2"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ロボットと一緒にジェットコースター乗りたいって思ってたりしてにゃ。",
    "facialExpression": "苦笑い",
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
    "characterName": "イヌ子",
    "text": "えぇ！ネコ美ちゃんがそんなこと言うなんて、意外！でも、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "それってすごくいいことだと思うよ！ロボットと一緒に遊ぶのって、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "新しい友達ができるみたいでわくわくするもんね！",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "しょうがないにゃ、今回はイヌ子の言う通り、",
    "facialExpression": "ドヤ顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ロボットの遊園地ブームは肯定的な現象ってことで。でも、",
    "facialExpression": "ドヤ顔",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ロボット専用の施設も大事にするべきだと思うけどにゃ。",
    "facialExpression": "ドヤ顔",
    "facing": "camera:0"
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
    "characterName": "イヌ子",
    "text": "ふふっ、ネコ美ちゃんと意見が合ってよかった！そして、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "みんなも意見を聞いてくれてありがとう！",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "今日のフィクション討論会はここまでだけど、",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "イヌ子",
    "text": "また次回も楽しい話題でお会いしようね！バイバーイ！わん！",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "ええ、今日はこれでおしまいにゃ",
    "facialExpression": "あくび",
    "facing": "camera:0"
  }
}
{
  "command": "TalkScript",
  "data": {
    "characterName": "ネコ美",
    "text": "また次回も面白い討論をしようにゃ。それじゃあ、お疲れ様でした！",
    "facialExpression": "あくび",
    "facing": "camera:0"
  }
}
```
