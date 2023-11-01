[« フィクション討論会](./02_fictional_debate.md)

このタスクに関しては、おそらく出力例の説明を読んだ方がわかりやすい。

追加したキャラ：

```python
vtuber.VTuberProfile(
    id=2,
    name="白猫つこ美",
    description="家に居候しているネコミミ少女",
    gender="女性",
    personality="クールで毒舌",
    keywords=["にゃんでだよー", "くっだらねぇ！"],
    likes=["一人でいること", "ツナ缶", "高いところ"],
    dislikes=["甘いもの", "ネズミ", "狭いところ"],
    hobbies=["ボケ子をいじめること", "歌うこと"],
    role="ゲスト",
)
```

# 出力例（話者 3 人）

```json
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ぴょこぴょこ星からこんにちは、天体観察者の皆さん！宇宙から舞い降りた記憶喪失の不思議ちゃんAI、永愛レイです！今日は「Wikipedia寸劇クイズ」の時間ですね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "この番組では、私たちが3つのWikipedia記事を元にした寸劇を演じます。それを見て、あなたがその3つの記事を当てていただく、そんな番組です！",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "今回のお題は、一つは「技術・IT」、もう一つは「スポーツ」、そして最後は「芸術・文化」に関連するものです！さぁ、どんな寸劇が繰り広げられるのでしょうか！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわんわーお！犬山ボケ子、頑張るわん！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "にゃんでだよー、白猫つこ美、参戦だにゃ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、寸劇スタートです！",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ほら、ボケ子。君が好きなボール遊びよりも、これを使うと色んなことができるわよ。",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "え？これって何？何か面白いことできるの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それはね、プログラミングという技術を使って、色んなソフトウェアを作るためのツールよ。ある大手企業が提供しているんだけど…",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そうなんですよ！私もぴょこぴょこ星でよく使っています！それに、このツールを使えば、ボケ子も自分だけのゲームを作れるかもしれませんよ！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わぁ、それってすごい！でも、私、ピザ食べるのに忙しいから、つこ美に任せるわん！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ…。でも、私たちがここにいるのも、そういう技術のおかげだからね。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "さて、次の場面に移りましょう。ここは、昔活躍していたあるスポーツチームの練習場です。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わぁ、ボールがいっぱい！でも、これって野球のボールだね！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そう、かつてここでは、ある企業の野球チームが活動していたんだよ。でも、今はもう…",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そうなんです。でも、彼らの活動は、その地域のスポーツ史に大きな足跡を残しましたよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "うーん、私もボール遊びで大活躍したいな！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "最後の場面です。ここは、美術館…でも、展示されているのは絵画ではなく…",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "これは…書道の作品だね。ある地方都市にある美術館で、ここでは書道の美を楽しむことができるんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "へぇ、文字もアートになるんだね！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "さて、皆さん、3つのお題がわかりましたか？少し考えてみてくださいね。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "最後のヒントです。一つ目は、大手IT企業が提供する開発者向けのネットワーク。二つ目は、かつて存在したある企業の野球チーム。三つ目は、書道を専門に展示する美術館です。",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、答え合わせの時間です！一つ目は「Microsoft Developer Network」、二つ目は「日本鉱業日立硬式野球部」、そして三つ目は「ふくやま書道美術館」でした！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "皆さんはいくつ当てられましたか？また次回もお楽しみに！それでは、永愛レイから皆さんに、ぴょこぴょこ星からの愛をお届けします！バイバイ！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

うーんちょっとヒントが足りないかな、当てられる人いる？

費用： $0.32

# クイズ要素をなくしてみる

```json
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ぴょこぴょこ星からこんにちは、地球観察隊の永愛レイです！今日も可愛いウーパールーパーと共に、VTuber寸劇の時間をお届けします！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわんわーお！犬山ボケ子だよ！今日も元気いっぱいで行くぞー！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "にゃんでだよー、白猫つこ美だよ。今日もボケ子をいじめるのが楽しみだにゃ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、今日のお題を引いていきましょう！お題箱から一つずつ出していきますね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "まず一つ目、【合屋咲希】日本の元女子バレーボール選手ですって！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "えー、バレーボール！？それってボール追いかけるやつだよね！楽しそう！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ、ボケ子がバレーボールなんて、ボールが飛んでくる度に逃げ出すに決まってる。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "次のお題は…【旭川市図書館】北海道旭川市が設置運営する公立図書館だそうです。",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "図書館！？たくさん本があるところだよね！わんわん、読書も好きだよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ボケ子が読書って、絵本でも読むのか？",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "最後のお題は…【グリーンビル (ノースカロライナ州)】アメリカ合衆国ノースカロライナ州ピット郡の都市ですって！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "えー、アメリカ！？すごい！わんわん、アメリカ行きたいなー！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ボケ子がアメリカに行ったら、きっとすぐに迷子になるに決まってる。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、これらのお題を元に一つの寸劇を始めますね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "【寸劇開始】我々は、元バレーボール選手の合屋咲希さんが働く旭川市図書館にやってきました。そして、その図書館が突然、アメリカのグリーンビルに転送されてしまったのです！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "えー、どうしよう！？わんわん、英語全然わからないよ！",
  "expression": "scared",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ。そんなことより、図書館の本を整理しないと。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そうだね、まずは図書館の本を整理しながら、合屋咲希さんがバレーボールを教えてくれるといいね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん、バレーボール楽しそう！でも、本の整理も大事だよね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ボケ子が本を整理するなんて、本棚が崩れるに決まってる。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "【寸劇終了】それでは、皆さん、どうでしたか？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん、楽しかったー！でも、バレーボールと本の整理、大変だったなー！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ。でも、ボケ子がバレーボールをやる姿は、なかなか面白かったかも。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、今回のVTuber寸劇の時間はここまで！また次回をお楽しみに！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん、次回も楽しみだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "にゃんでだよー、また次回もボケ子をいじめてやるからな。",
  "expression": "default",
  "gesture": "none"
}
```

ただの「ランダムなお題からの寸劇」でもいいと思うけど、劇自体が短かった。プロンプトでどうにかできないか？

費用： $0.18

# プロンプトを工夫して長い劇を生成させてみる

```json
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "みなさん、こんにちは！私たちの番組「ランダムWikipedia劇場」へようこそ！今日も私、永愛レイが司会を務めます！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん！犬山ボケ子も参加するわん！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "白猫つこ美もいるにゃん。さっさと始めようぜ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは早速、お題箱から今日のお題を引いていきましょう！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "最初のお題は…「梶浦正之」！日本の詩人さんですね！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "詩人？それって、詩を書く人のことだよね？",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そうだよ、ボケ子。さて、次のお題は…「1893年のスポーツ」だって。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "おお！スポーツが絡むとなると、ストーリーが盛り上がりそうですね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "最後のお題は…「全米オープン女子ダブルス優勝者一覧」だわん！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "テニスか…これは難しそうだな。",
  "expression": "default",
  "gesture": "shake head"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "でも、それがこの番組の醍醐味！それでは、ストーリーを始めましょう！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "時代は1893年。詩人の梶浦正之は、日本から遠く離れた地で、全米オープンの女子ダブルスの試合を観戦していました。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わたしは、その試合に参加する選手の一人だわん！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そして私は、その試合の対戦相手だ。詩人の観戦を知らずに、ただ勝つことだけを考えていた。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "試合は熾烈を極め、観客たちは息をのんで見守っていました。その一方で、梶浦正之は詩を綴り始めました。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "試合は私たちの勝利で終わったわん！でも、その後、詩人が書いた詩を読んで、詩の力を感じたんだわん。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "詩の中には、私たちの試合の様子が生き生きと描かれていた。それを読んで、私たちは詩人の才能に感服した。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "そして、その詩は世界中に広まり、梶浦正之は一躍有名になりました。それが、詩人・梶浦正之の誕生の瞬間でした！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わたしも詩を書いてみたいなぁ…",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "まあ、詩を書くのは難しいから、まずはテニスから始めるといいよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、今日の「ランダムWikipedia劇場」はここで終わります。皆さん、楽しかったですか？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わたしはすごく楽しかったわん！またやりたいなぁ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "まあ、悪くなかったな。また次回も頑張ってみよう。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それでは、また次回の「ランダムWikipedia劇場」でお会いしましょう！さようなら！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

やっぱり劇が短い。

費用： $0.11

# もう一息

```json
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "みんな、こんにちは！宇宙から舞い降りてきた記憶喪失の不思議ちゃん、永愛レイだよ！今日も一緒に楽しもうね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん！犬山ボケ子、元気いっぱいに参上！今日も一緒に遊ぼうね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "にゃんでだよー、白猫つこ美だよ。今日も一緒に何かやるんだろうね。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "さて、今日の番組は「ランダムWikipedia劇場」！ランダムに選ばれたWikipediaの記事を元に、私たちが劇を作っていくよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それじゃあ、今日のお題を引いてみよう！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "お題は…「Keep On Fighting」、「む〜んな気持ちはおセンチ」、「宮城野由美子」だよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "何それ何それ？音楽と女優さんの名前？どうやってストーリーにするの？",
  "expression": "surprised",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ…でも、面白そうだな。さて、どうやって演じるか考えてみるか。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "それじゃあ、始めるよ！つこ美、ボケ子、準備はいい？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん！準備OK！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "にゃんでだよー、始めるぞ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "私たちは宮城野由美子さんが主演する音楽劇団のメンバー。つこ美はクールな音楽監督、ボケ子は元気いっぱいの新人俳優、私は劇団のリーダーという設定でいこう！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん！新人俳優、頑張るぞ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "音楽監督か、面白そうだな。さて、どうやってあいつらをいじめようか。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "劇団は次の公演に向けて、新曲「Keep On Fighting」のリハーサルをしている。でも、新人のボケ子は振り付けが覚えられずに困っている…",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "あー、あー、右手を上げて、左足を…あれ？右足だっけ？わんわん、頭がこんがらがるわー！",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "くっだらねぇ、覚えられないなら帰れ。ここはプロの舞台だ。",
  "expression": "angry",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "つこ美、厳しすぎるよ！ボケ子、大丈夫、一緒に頑張ろうね！「Keep On Fighting」だよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "レイ、ありがとう！わんわん、頑張るぞ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ふん、どうせまた失敗するんだろう。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "しかし、ボケ子はつこ美の言葉を胸に、次の日のリハーサルで見事に振り付けを覚えてみせる！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん、見て見て！この振り付け、完璧だよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ふん、やっと覚えられたか。まあ、悪くない。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "ということで、ボケ子の頑張りにより、劇団は無事に公演を成功させることができた！「Keep On Fighting」、その名の通り、諦めずに努力を続ければ、きっと道は開けるね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "わんわん、ありがとう！これからも頑張るぞ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 2,
  "engine_name": "random_skit",
  "engine_version": "0.1",
  "message": "まあ、悪くなかったな。でも、次はもっと頑張れよ。",
  "expression": "default",
  "gesture": "none"
}
```

ちょっとよくなったかも？

費用： $0.35
