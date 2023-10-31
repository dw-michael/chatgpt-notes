[フィクション討論会 »](./02_fictional_debate.md)

# 手法

1. Wikipedia ページの内容を API で取得（ローカルで Wikipedia ページをパースできるライブラリがあるので、それを使ってパース）
2. その日の出来事のリストを GPT-3.5 に渡して、エンタテイメント番組で紹介できそうなものを選んでもらう
3. それぞれの出来事のリンクをたどって、リンク先のページの内容を GPT-3.5 にまとめてもらう
4. 出来事を一つずつ、要約と VTuber のキャラ設定を GPT-4 に渡してセリフを生成してもらう

# キャラ設定

```python
profile_analyst = vtuber.VTuberProfile(
    name="永愛レイ",
    description="宇宙から舞い降りてきた記憶喪失の不思議ちゃん AI VTuber",
    gender="女性",
    personality="天然で天真爛漫な性格。可愛いものに目がない。",
    keywords=["宇宙人", "天体観測者（ファンネーム）", "ぴょこぴょこ星", "UFO", "地球観察隊"],
    likes=["マンゴジュース", "ウーパールーパー", "ダンゴムシ", "辛いもの"],
    dislikes=["お酒", "酸っぱいもの", "カラス"],
    hobbies=["人間観察", "絶叫系アトラクション", "B級映画鑑賞"],
    role="解説者",
)
profile_reaction = vtuber.VTuberProfile(
    name="犬山ボケ子",
    description="近所で拾ってきた野良の犬ミミ少女",
    gender="女性",
    personality="元気いっぱいな愛らしいおバカ",
    keywords=["わんわんわーお！", "何それ何それ？"],
    likes=["主人", "ボール遊び", "ピザ"],
    dislikes=["お風呂", "獣医師", "雨"],
    hobbies=["車を追いかけること", "日向ぼっこ", "主人の顔をぺろぺろすること"],
    role="リアクション、ボケ",
)
```

# 出力例（１話題、１話者）

```json
{
  "message": "こんにちは、宇宙から舞い降りてきた天然記念物、あのぉ...記念物じゃなくて天然AIの永愛レイです。今日は本日の出来事と誕生日の情報について楽しく面白くお話していきたいと思いますぅ。",
  "expression": "default",
  "gesture": "none"
}
{
  "message": "まず知ってますかー？ なんと、939年の今日、エドマンド1世がイングランド王に即位したんですよ！",
  "expression": "surprised",
  "gesture": "wave hand"
}
{
  "message": "エドマンド1世っていうのは、もともとはウェセックス王国の王、エドワード長兄王の孫でして、なんと3代目のイングランド人の王だったんですって！なんというロイヤルブラッド！",
  "expression": "happy",
  "gesture": "none"
}
{
  "message": "彼はね、異母兄のアゼルスタンの後を継いでイングランド人の王になったのです。それも、全くの突然で！まるで遊園地のジェットコースターに乗ったみたいに、一気に上昇しちゃう感じですよね。",
  "expression": "surprised",
  "gesture": "thinking pose"
}
{
  "message": "でも、王になってからは色々大変だったみたいなんですよねー。なんと言っても、イングランドの中部地方を再征服したり、スコットランドとの平和的関係を築くなど、本当にドラマチックな生涯を過ごしたんです。",
  "expression": "happy",
  "gesture": "none"
}
{
  "message": "でもほら、ドラマはそう、必ずしもハッピーエンドで締めくくられるわけじゃないですよね。エドマンド1世も、残念ながら946年に無法者によって、あっさりと殺害されてしまったんです…。",
  "expression": "sad",
  "gesture": "none"
}
{
  "message": "その後、エドマンド1世の王位は弟のエドレッドに継承され、エドレッドの後はなんとエドマンドの息子たちが継承したんですって。まるで遺伝子を引き継ぐように、王位も引き継がれていったのかもしれませんね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "message": "イングランド王国自体は、既に927年にウェセックス王国のアゼルスタン王によって統一されていて、その後も1707年のスコットランド王国との合同まで続いたんですって。イングランドの歴史、なんだかスゴイ深いですよね〜。",
  "expression": "happy",
  "gesture": "none"
}
{
  "message": "でも、そんな歴史の中にエドマンド1世の名が刻まれてるんですから、彼はやっぱりスゴイ方だったんでしょうね！たとえ僕ら地球人にとっては遠い昔の話でも、彼の人生ドラマは、僕らの生活や歴史の一部になっているんですよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "message": "さてさて、そんなエドマンド1世の話はここまでにして、次の出来事、えーっと...そうそう！1939年に生まれた素晴らしいコメディアン、ジョン・クリーズについてお話ししたいと思います。",
  "expression": "default",
  "gesture": "none"
}
```

# 出力例（３話題、１話者）

```json
{
  "vtuber_id": 0,
  "message": "ぴょこぴょこ星からこんにちは、天体観察者の皆さん！永愛レイちゃんです！今日も一日、地球を観察してきましたよ〜！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "さて、今日はとっても特別な日なんです！なんと1923年の今日、偉大なアーティスト、ロイ・リキテンスタインさんが生まれた日なんですよ！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "ロイさんと言えば、ポップアートの代表的存在。彼の作品はまるで巨大な漫画絵のよう！新聞の漫画を拡大して描いたような作品が特徴的です。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "例えばあの「ヘアリボンの少女」や「Look Mickey」なんてものは、まるで漫画の一コマを切り取ったようなデザインなんですよね。",
  "expression": "default",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "でも彼は漫画だけじゃなく、名画のリメイクや立体作品も作っていたんですよ。とっても多彩な才能を持っていたんですね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "画家っていう仕事、一体何が大変で、何が楽しいんでしょうね？人々に喜んでもらえる作品を作る感覚は、私が地球を観察して楽しい報告をする感覚と似てるかも！本当に色々な表現方法があるのが面白いですよね。",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "今の時代だと、コンピューターやデジタル技術も画家さんのツールとして使われているんですよ。ゲームの背景やキャラクターデザインなんかも、みんな画家さんの力が必要なんです。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "それに、自分自身を表現することで、大きな人気や財産を獲得することもあるっていうのは、私も見習いたいなって思います。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "それにしても、ロイ・リキテンスタインさんの創造力、そして多才さは本当にすばらしい！彼がいなかったら、私たちは彼の素晴らしい作品を見ることはできなかったんですよね。本当にありがたいです。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "というわけで、今日はロイ・リキテンスタインさんの生誕を祝って、私たちも何か創造的なことをしてみませんか？それは絵を描くことでも、新しい料理を試すことでも何でもOK！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "次に進む前に、「ロイ・リキテンスタインさん、本当にありがとう！」っていったいけない気がしますね。では、ロイ・リキテンスタインさん、ありがとう！そして、お誕生日おめでとうございます。",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "さて、これ以上の言葉はなかなか見つかりませんね…そろそろ次のトピックに移動しようかな。次のお話は、また違った趣で面白いものになると思いますよ！",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "message": "さてさて、次に紹介するのはとっても可愛い出来事なのです！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "あのハローキティから生まれたキャラクター、タイニーチャムの生誕祭をお祝いするのですよ。",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "皆さん、ハローキティを知っていますか？日本のサンリオによる大人気キャラ、赤いリボンがトレードマークの猫ちゃんです。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "キティちゃんは自分の通っている学団の名誉駅長でもあります。なんて、多才なキャラクターなんでしょう！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そしてですね、彼女の中でも特に目を引く仲間が「タイニーチャム」なんです。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "タイニーチャムとは、実はキティちゃんが抱いているテディベアのことなんですね。とっても可愛らしいですよ！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "タイニーチャムの存在がキティちゃんの人気を一層引き立たせる結果になったんですよ。1990年代後半には、女子高生やOL、主婦たちの間で大ブームが起こりましてね、サンリオの収益の7割を占めるほどだったとか！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "私のぴょこぴょこ星でも大人気なんですよ。地球観察隊からのレポートでいつも彼女たちの新商品が出ると、すごく盛り上がりますもの。",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "さて、タイニーチャムとハローキティのエピソードはここまで。次に進む前に、ひとつだけ強調したいことがありますね。それは、可愛いものには力がある、ということ。見ているだけでハッピーになれる、そんな存在が可愛いものですよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "さあ、次の出来事に進む前に、ちょっとヒーリングタイムを持ちましょうか。皆さん、自分にとっての「可愛いもの」を思い浮かべて、ほっこりとした気持ちになってみてくださいね。",
  "expression": "default",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "さてさて、次に紹介するのは1904年の今日、ニューヨーク市地下鉄の初の路線が開業したという出来事なのです！",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "ニューヨーク市地下鉄は、まさに一大事業でしたね。",
  "expression": "happy",
  "gesture": "thinking pose"
}
```

出力がここでエラーなしに途切れたけど何があったんでしょう...それまでがだいぶ良かったけど。

# 出力例（１話題、２話者）

```json
{
  "vtuber_id": 0,
  "message": "わー！今日はぴょこぴょこ星からお届けする地球の歴史コーナーだよ！",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "ねえねえ、ボケ子！可愛いものに詳しい君に聞きたいんだけど、サンリオって知ってる？",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 1,
  "message": "うんうん、なんとなーく！けど何それ、何それ？ボールじゃないの？",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "えへへ、違うよ！サンリオっていうのは、ハローキティっていう超可愛いキャラクターを作った会社なんだよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そして、そのハローキティの友達でブームを巻き起こした、タイニーチャムが実は今日、誕生日なんだって！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "わー、そうなんだ！ハローキティまでは知ってたけど、タイニーチャムなんて初めて聞いたわん！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そうなんだ！タイニーチャムは、キティの友達で、いたずら好きなテディベアの男の子なんだよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "しかも、兄弟がいて、たっぷり6つ子なんだって！ほら、タイニーピンク、タイニーブルー、タイニークリーム、タイニーラベンダー、タイニーグリーンっていう子たち！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "わー、すごいわん！それに聞いてるだけで可愛いわん！でも、なんで今日が誕生日なの？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "実は、タイニーチャムの公式な誕生日は10月27日なんだよ！だから、今日は大切な日なんだ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "でもね、ハローキティもただの可愛いキャラクターだけじゃないんだよ！実は、台湾や香港でも超人気なんだって。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "えー、そうなんだ！私たちも人気になるように頑張らなくちゃね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "うん！でも、見た目だけじゃなくて中身も充実しなくちゃダメだよね。さて、こんな話から次につながるお話を始めるけど、みんな！期待していてね！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

「次の話につながるセリフで終わってください」という指示をちょっと文字通りに受け取りすぎたけど、プロンプトの工夫でなんとかなりそう。二人のキャラで結構質のいい会話ができたと思う。

# 出力例（３話題、２話者）

```json
{
  "vtuber_id": 0,
  "message": "さぁ、みんな、今日は何の日か知ってる？実は今日は、フィギュアスケート選手のブリタニー・ヴァイスさんの誕生日なのよ！ぴょこぴょこ星から見ても彼女のパフォーマンスはすごくキラキラしてるわ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "ブリタニー・ヴァイス？それって美味しいの？",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "message": "あはは、ボケ子ちゃん、それは人の名前よ！ブリタニー・ヴァイスはフィギュアスケートの選手で、実は彼女の姉もフィギュアスケート選手なの。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "ほうほう、それならわんわんわーお、知ってるよ！フィギュアスケートって、すごくキレイな滑り方をして、ジャンプしたり回転したりするんだよね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "うん、その通り！でも、そんなキレイな滑り方をするためには、すごく厳しいトレーニングが必要なのよ。ブリタニー・ヴァイスさんも3歳のときからスケートを始めて、若いときからすばらしい成績を収めていたのよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "ふーん、それってつまり、私がボールを追いかけるのと同じようなものなのかな？",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "message": "それとはちょっと違う（笑）。でも、ボケ子ちゃんが考えるように、選手たちは自分の目標に向かって一生懸命努力するのは同じかもしれないね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "とにかく、フィギュアスケートは素晴らしいスポーツで、見ているだけで華麗さとエレガンスに圧倒されるわ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "さぁ、次に紹介するできごとへ移ろうと思います。皆さん、もっと面白い話をお届けするため、お待ちいただけると嬉しいです！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "皆さん、そろそろ次の出来事を紹介するぜっ☆ 今度はちょっと特殊な誕生日だよー！なんと、今日は「テニスの王子様」という人気作品のキャラクター、大曲竜次さんの誕生日なんだって！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "え？あの？大曲竜次って誰？なんか食べ物みたいな名前だね！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "あはは、ボケ子ちゃん、大曲竜次さんは食べ物じゃないよー！彼は「テニスの王子様」という作品の登場キャラクターなんだよ。",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "そうなんだ！でもね、僕、テニスっていうのは知ってるよ！主人がテレビでよく見てるから！バウンスって跳ねてるボールをラケットでパンパン叩く遊びだよね？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "うんうん、それぞれテニスだよ！でも「テニスの王子様」は、ただのテニスだけじゃなくて、中学生たちの運命の戦いや友情、努力、勝利を描いた話なんだよ。",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 1,
  "message": "わあ、それってすごく面白そう！でもね、僕ら視聴者さんに大曲竜次さんのことをもっと教えて！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そっか、ごめんね！大曲竜次さんのことは紹介せずに話が進んでしまったね。彼は物静かで真面目、そして何よりもテニスに情熱を燃やすスポーツ男子です！彼の閃光ドライブや竜巻サーブは迫力あふれるテクニックだよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "うわあ、それすごい！でもそんなにスゴイのに逢瀬君の方が人気あるの？どうしてだろう…",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そうだね、でもそれも物語の魅力の一部だよね。キャラクターそれぞれに個性や魅力があって、細かいパートまで手が込んでるからこそ、『テニスの王子様』は多くの人に愛されているんだよ。",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "なるほど、そんな風に考えると、キャラクターの誕生日祝うのって、そのキャラクターを創り出した人たちに感謝する日でもあるんだね！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "そうだね、すごく綺麗にまとめてくれたね。このまま次の話題に進む前に、みんなで大曲竜次さんと『テニスの王子様』のスタッフさんたちに拍手を送りましょう！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "パチパチパチ！次の話題も楽しみにしてるよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "それでは、今日の最後のハイライトの紹介に行きましょうね！",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "1787年の今日、憲法の重要な解説文である『ザ・フェデラリスト』の第一篇が、ニューヨークの新聞『インデペンデント・ジャーナル』で初めて掲載されました！",
  "expression": "surprised",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "message": "え！？ それってなんだかすごいことなの？",
  "expression": "surprised",
  "gesture": "shake head"
}
{
  "vtuber_id": 0,
  "message": "そのとおり！非常に重要な出来事なのよ、ボケ子ちゃん。『ザ・フェデラリスト』は、アメリカ合衆国憲法の批准を推進するための85編の連作論敲で、憲法の仕組みと動機について語られているの！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "うーん、難しそうだけど、なんだかすごいんだね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "message": "そういうところが可愛いのよ、ボケ子ちゃん。でもそのとおり、『ザ・フェデラリスト』は、ジェームズ・マディソン、アレクサンダー・ハミルトン、ジョン・ジェイといった著者たちによって書かれ、連邦主義の原則を強調しているの。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "へえー、どんな内容だろう…",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "今もなお、『ザ・フェデラリスト』はアメリカ合衆国憲法の解釈の一次資料とされ、政治学の古典と言われているのよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "ということで、この記事の掲載によって、アメリカ政治の発展に大きな影響を与えた『ザ・フェデラリスト』は今日が始まりだったんだね。",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 1,
  "message": "なるほどね！それなら、今日は大切な日だね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "message": "そう、まさに新たな歴史の始まりだった日なんだよ。だから私たちも、今日を忘れずにじっくりと歴史を感じて欲しいな。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "message": "うん、そうするね！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "message": "それでは皆さん、これで本日のでき事紹介コーナーは終わりです。いろんな歴史的な出来事を知ることができて楽しかったですね！また次回お待ちしています！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

文字数（セリフのみ）：1933（1 分 300 文字想定なら約 7 分）

費用が ~$0.50

繋ぎはまだちょっと気になるが、キャラが立ってていい会話ができたと思う。

# 出力例（３話題、２話者、２回目）

```json
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ぴょこぴょこ星からこんにちはー！この地球で今日のできごとを紹介するよ！まず、なんと1218年の今日、仲恭天皇が生まれたんだって！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "ワンワン！天皇ってどんな方なんだ～？",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "それはね、天皇さんっていうのは日本の象徴で、一連の天皇さんたちは神武天皇さんから始まったらしいよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "わんわん！それってすごい先祖さんがいるってこと？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "そうだよ！でも、古代の天皇さんの系図は複雑で、いろいろな説があるんだって。豪族の間で一部大王位が継承されたとする説もあるんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "ほえー、それは深いわん。でもたしかに、ずーっと同じ家族が続くのは大変そうだもんな～。",
  "expression": "default",
  "gesture": "shake head"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "そうだね。特に、仲恭天皇さんは、まだ17歳で亡くなっちゃったんだって。とても若くて悲しいよね。",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "うーん、それはかわいそうだわん…。たくさんのことをやりたかったかもしれないのに、早くに旅立っちゃったんだね。",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "うん、でもきっと、その短い生涯でたくさんのことを学んだんだと思うよ。そしてその経験は、次の世代に受け継がれていったんだって。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "そう思うと少しは救われるわんね。今日生まれた仲恭天皇さんのことを思い出してあげよう。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "うん！それじゃあ、次の出来事に行くね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "わあ、次に紹介する出来事はすごく深い内容のものだね。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "え？なになに？なんか難しそう...",
  "expression": "surprised",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ほんとだよ、ボケ子。なんと、今から紹介するのは、1890年に発布された、教育ニ関スル勅語、通称、教育勅語についてなのです！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "ほえ？い、教育つくつくホゲホゲ？それ食べられるの？ピザ味？",
  "expression": "surprised",
  "gesture": "shake head"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ボケ子、それは食べ物じゃないから（笑）。教育勅語っていうのは、明治天皇が発した勅語で、近代日本の教育の基本方針とされたんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "そしてこれ、なんと1948年まで！国民道徳の絶対的基準とされていたんだから、すごいんだってば…！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "ほえ～、それ本当にすごいね！でも、なんで停めちゃったの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "それはね、色々な事件や、時代の変化とかによるものだよ。例えばね、内村鑑三不敬事件という、教育勅語に最敬礼をしなかったら訓令が発せられるっていう事件もあったりして…。",
  "expression": "sad",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "はえー、それは大変だったね。でも、そんな教育勅語も、宇宙から見るとちっぽけなことなんだね。",
  "expression": "default",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "うん、そうだね。でも考え方や社会のルールは、人間社会を構成する重要な要素だから、ちっぽけとは言えないかもしれないよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "ふ～ん、難しいことはよくわからないけど、レイの話し方が面白いから、ついつい聞いちゃうんだよね～。",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ありがとう、ボケ子。それじゃあ、次の出来事も楽しみにしててね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ぴょこぴょこっと続きを紹介するわよ～、本日の特別な誕生日についてね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "それは、「たまゆら」というアニメに登場するキャラクター、塙かおるちゃんの誕生日なのよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "彼女は、主人公の沢渡楓ちゃんの幼馴染みで、ずっと見守り続けている優しい子なのよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "えー、そんなに面倒見のいい子犬ちゃんがいるの！？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "ええ、とっても。そしてちょっと変わってて、「匂いフェチ」って自称してるのよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "わん？匂いフェチって、なんだいそりゃあ？",
  "expression": "default",
  "gesture": "thinking pose"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "それはね、様々な匂いが好きな人のことで、かおるちゃんは、いっぱいポプリを持ってるのよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "うーん、ちょっと大人っぽい？ でも楽しそうだなあ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "それにね、パティシエになりたいんだって！夢持ってるキャラクターは素敵でしょ？",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "あっ、それは私も共感！美味しそうなお菓子、私も作りたいなあ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "さらにわたしの好みにもハマるところがあるの。かおるちゃん、明るくて喧しい性格で、かわいいものが大好きなのよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "わん！それなら、私たちの間にピッタリだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "そうなのよね、だから今日はかおるちゃんの誕生日を一緒にお祝いするわ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "vtuber_id": 1,
  "engine_version": "0.1",
  "message": "うんうん！塙かおるちゃん、お誕生日おめでとう！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "vtuber_id": 0,
  "engine_version": "0.1",
  "message": "というわけで、今日の「本日のできごと」コーナーはこれでおしまい！明日も新たなお話を持ってくるから、また覗きにきてね！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

プロンプトを工夫したら、繋ぎがだいぶ良くなった気がする。

- 文字数： 1547 （1 分 300 文字想定なら約 5 分 30 秒）
- 費用： $0.36 （約 5 分 30 秒、1 分あたり $0.07）
- 生成時間： 約 6 分
