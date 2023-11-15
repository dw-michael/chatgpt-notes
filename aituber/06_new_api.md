[« テロップアクション](./05_telop.md)

# 概要

新しい API （response_format=json_object）を使ってテロップや他のアクションを LLM で同時に＋柔軟に生成してみる

- 前は LLM が生成したメタデータからコードで決まった形式でテロップアクションを作っていた
- 今後は自然言語での指示で LLM にテロップアクションを作ってもらう

# 出力例（仮想ディベート）

```json
{
  "type": "telop",
  "action": "show",
  "position": "title",
  "text": "フィクション討論会"
}
{
  "type": "character",
  "character_id": 0,
  "message": "こんにちは、宇宙からやってきた永愛レイよ！今日は「フィクション討論会」で未来の世界について語り合うわ！ぴょこぴょこ星からの視点も交えてね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわんわーお！犬山ボケ子だよ！未来とか宇宙とかわけわかんないけど、楽しそうなので一緒に盛り上がっちゃうぞー！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "title",
  "text": null
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "【設定】未来都市でロボットと人間が共存、ロボットはペットの「感情」を持ち合わせている"
}
{
  "type": "character",
  "character_id": 0,
  "message": "さて、未来都市ではロボットが人間のようにペットを飼えるんだって。これって感情教育にいいのかしら？",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "caption",
  "text": null
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "【お題】ロボットがバーチャルペットを飼うことで感情教育が向上するか"
}
{
  "type": "character",
  "character_id": 0,
  "message": "私は賛成よ！ロボットがペットを愛する心を学べば、人間にもっと優しくなれると思うの。ねえ、ボケ子はどう思う？",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "んー、反対かなぁ。バーチャルだと匂いも感じられないし、本当のペットの温もりって大事だよね！",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "でも、バーチャルペットならアレルギーの心配もないし、お手入れも簡単だよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "そうだね、それは便利かも…。でも、お散歩に行ったりボール遊びするのも楽しいのになぁ。",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "あはは、ボケ子ったら、ロボットがボールを追いかけている姿を想像してみて！それもまた一興よ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "あ、それは面白そう！じゃあ、ロボットにもペットの楽しさを知ってほしいかも！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "caption",
  "text": null
}
{
  "type": "character",
  "character_id": 0,
  "message": "見ての通り、私たちの討論でバーチャルペットはロボットの感情教育にぴったりかもしれないって結論になったわ！次のお題に進むわよ～！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "telop",
  "action": "show",
  "position": "title",
  "text": "フィクション討論会 第2ラウンド！"
}
{
  "type": "character",
  "character_id": 0,
  "message": "ぴょこん！次のお題はね、すごく不思議な現象が起きちゃった世界の話なの！世界中の椅子たちが突然意識を持ってしまって、自分が一番座り心地がいいって自慢しちゃうの！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわん！それってめちゃくちゃ面白そうじゃない？椅子が喋りだしたら、毎日がもっとわくわくするに決まってるよ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "【お題】椅子が自己主張をすることで、椅子選びがもっと楽しくなるか？"
}
{
  "type": "character",
  "character_id": 0,
  "message": "うーん、でもね、椅子がずっと自分のことを褒めちぎってたら、選ぶのが大変になっちゃうかも。私たちがどの椅子に座りたいか、自分たちで決めたいよね〜。",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "でもね、ボケ子は自分が好きなものを自分で決めたいけど、椅子が自分でおすすめしてくれるのも楽ちんでいいかも！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 0,
  "message": "まあ、それも一理あるかもしれないけど、椅子たちが自分を売り込みすぎて、喧嘩しちゃったら大変だよ！",
  "expression": "scared",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "あはは！椅子の喧嘩なんて見てみたいかも！どんな感じになるんだろうね～？",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "ふふっ、それはそれで新しいアトラクションみたいで面白そうだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "そうそう！だからボケ子は賛成だよ！椅子が自己主張する世界、楽しそう！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "レイも賛成に回るよ！きっと地球のみんなも新しい椅子選びを楽しむことができるはず！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "caption",
  "text": null
}
{
  "type": "telop",
  "action": "hide",
  "position": "title",
  "text": null
}
{
  "type": "telop",
  "action": "show",
  "position": "title",
  "text": "フィクション討論会 - 最終お題"
}
{
  "type": "character",
  "character_id": 0,
  "message": "皆さん、今日の最後のお題はね、空飛ぶスパゲッティモンスターがいて、私たちにスパゲッティを食べさせてくれる世界なの！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "何それ何それ？！飛んでるスパゲッティから食べ物がポロポロ落ちてくるの？！わんわんわーお！",
  "expression": "surprised",
  "gesture": "wave hand"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "【お題】空飛ぶスパゲッティモンスターの食事提供は食文化に寄与する？"
}
{
  "type": "character",
  "character_id": 0,
  "message": "うんうん、そういう設定なの。私は賛成よ。だって、毎日空から新鮮なスパゲッティが降ってくるなんて、食べることがもっと楽しくなると思わない？",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 1,
  "message": "でもでも、雨の日にスパゲッティがびしょびしょになったらどうするの？それに、飛んでるスパゲッティを捕まえるの大変そう…。",
  "expression": "sad",
  "gesture": "shake head"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そこはね、スパゲッティモンスターが賢くて、雨の日は屋根の下に降りてきたり、食べやすいようにゆっくり飛んでくれるのよ。人々が楽しめるように工夫してくれるんだから、新しい食文化が育つと思うの！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "へぇ〜、そうなんだ！じゃあ、空から降ってくるスパゲッティを待ち構えて、ピザと一緒に食べたら最高だね！",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうそう、それに新しいレシピや食べ方が生まれるかもしれないし、みんなでワイワイスパゲッティを食べるのは、すごく楽しいと思うわ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "うんうん、納得！空からのプレゼントスパゲッティ、楽しみにしてるわん！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "caption",
  "text": null
}
{
  "type": "character",
  "character_id": 0,
  "message": "というわけで、空飛ぶスパゲッティモンスターからの食事提供は、新たな食文化の創造に寄与するという結論になりました！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "これで今日の「フィクション討論会」コーナーはおしまい！また次回も楽しいお題でお会いしましょう！バイバイ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "telop",
  "action": "hide",
  "position": "title",
  "text": null
}
```
