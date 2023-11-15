[« Wikipedia レース](./04_wikipedia_race.md) | [テロップ同時生成 »](./06_new_api.md)

# 概要

テロップアクションを追加してみた。形式は仮だけど、配信画面にテキストを表示する最低限の機能があるといいと考えた。

# 出力例（Wikipedia レース）

```json
{
  "type": "telop",
  "action": "start",
  "position": "title",
  "text": "Wikipediaレースのコーナー"
}
{
  "type": "character",
  "character_id": 0,
  "message": "こんにちは、天体観測者のみんな！永愛レイだよ。今日はちょっと違った旅に出てみようと思うんだ。それはね、Wikipediaレース！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "telop",
  "action": "stop",
  "position": "title",
  "text": null
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "Wikipediaレースのルール"
}
{
  "type": "character",
  "character_id": 0,
  "message": "Wikipediaレースって何？って思う人もいるかもしれないから説明するね。これはね、ランダムに選ばれたWikipediaの記事からスタートして、記事内のリンクだけを使ってゴールの記事まで辿り着くゲームなんだ。最短ルートでゴールに辿り着いた人が勝ち！ただし、カテゴリページと曖昧さ回避ページの使用は禁止だよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "スタート：「第36回全国高等学校バスケットボール選抜優勝大会」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "今回のスタート記事は「第36回全国高等学校バスケットボール選抜優勝大会」だよ。バスケットボールの大会って、熱い戦いが繰り広げられるよね。私も地球のスポーツは大好きだから、興奮するわ～！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、ゴール記事は「X X X」。これは日本のロックバンド、L'Arc〜en〜Cielの38枚目のシングルなんだって。音楽からスポーツまで、地球の文化は本当に豊かだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "さあ、みんなも一緒にゴールを目指してみよう！レース、スタート！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "まずは、【第36回全国高等学校バスケットボール選抜優勝大会】の記事からスタートだよ。バスケットボールって地球のスポーツの中でもとっても人気があるよね。私もぴょこぴょこ星で試してみたいな～。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に辿ったのは【京都市立紫野高等学校】の記事。ゴール記事はL'Arc〜en〜Cielのシングルだから、音楽に関連した記事を選んでみたんだ。高校って地球では色んな部活動があるんだよね。音楽部とかあるのかな？",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「作曲家」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【作曲家】の記事を選んだよ。音楽に関連する記事を選ぶことで、ゴールのL'Arc〜en〜Cielのシングルに近づけるかなって思って。作曲家ってすごいよね、色んな音を組み合わせて一つの楽曲を作り上げるなんて。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「楽曲」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次は【楽曲】の記事へ。音楽に関連する記事を辿ることで、ゴールのL'Arc〜en〜Cielのシングルに近づける可能性が高いと思って。楽曲って一つ一つが作曲家の思いが詰まっていて、それを聴くことでその思いを共有できるんだよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「シングル」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【シングル】の記事へ。音楽、とくに大衆音楽における楽曲の販売単位だって。私たちが普段聴いている音楽って、こうやって作られているんだね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「スピッツ (バンド)」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【スピッツ (バンド)】の記事を選んだよ。スピッツも日本のロックバンドだから、L'Arc〜en〜Cielと何か繋がりがあるかもしれないよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「ハチミツ (アルバム)」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【ハチミツ (アルバム)】の記事へ。これはスピッツのアルバムだって。アルバムって一つの作品の中に色んな楽曲が詰まっていて、その全てを聴くとそのバンドの世界観が広がるんだよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「ロック (音楽)」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【ロック (音楽)】の記事へ。L'Arc〜en〜Cielもロックバンドだから、ここから何かヒントが見つかるかもしれないよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「ブルースロック」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【ブルースロック】の記事へ。これはロック音楽のジャンルの一つだって。音楽のジャンルって本当に色々あるんだね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「クリーム (バンド)」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【クリーム (バンド)】の記事へ。これもロックバンドだから、何か繋がりがあるかもしれないよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「カラフル・クリーム」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【カラフル・クリーム】の記事へ。これはクリームのアルバムだって。アルバムの名前も色々で面白いよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「ボブ・ディラン」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【ボブ・ディラン】の記事へ。ボブ・ディランはアメリカのミュージシャンで、彼の影響を受けたミュージシャンも多いんだよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「トラブゾン」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【トラブゾン】の記事へ。これはトルコの都市なんだって。音楽と地理、意外と繋がりがあるかもしれないよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「トルコ」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "次に【トルコ】の記事へ。トルコは西アジアに位置する国で、文化もとても豊かなんだって。音楽もその一つだよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「国民の父」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そして、【国民の父】の記事へ。これは、多くの国家において、独立期や発展期に活躍した象徴的な人物や政治的な指導者を指す言葉なんだって。音楽も人々に影響を与える力があるから、ここから何か見つかるかもしれないね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "現在の記事：「国家」\nゴール：「X X X」"
}
{
  "type": "character",
  "character_id": 0,
  "message": "最後に【国家】の記事へ。これは、「一定の領土と国民と排他的な統治組織とを供えた政治共同体」を指す言葉だって。音楽と国家、どちらも人々を繋げる力があるよね。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "start",
  "position": "caption",
  "text": "ゴール失敗"
}
{
  "type": "character",
  "character_id": 0,
  "message": "うーん、でも残念ながらゴールの「X X X」には辿り着けなかったみたい。でも、色んな記事を見て知識が増えたから、それも一つの収穫だよね！",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "今回は15ステップ使ったよ。みんなは何ステップでゴールに辿り着けたかな？コメントで教えてね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "stop",
  "position": "caption",
  "text": null
}
{
  "type": "character",
  "character_id": 0,
  "message": "それでは、今日のWikipediaレースはここまで！次回も一緒に色んな知識を深めていこうね！バイバイ！",
  "expression": "happy",
  "gesture": "wave hand"
}
```

ルートの最初の方のテロップが少し抜けていたが、全体的にはあっていた。

# 出力例（本日の出来事）

```json
{
  "type": "character",
  "character_id": 0,
  "message": "みなさん、こんにちは！私たちの配信へようこそ！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわんわーお！ボケ子も元気いっぱいだよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "（誕生日）1799年 - ジュール＝アンリ・ヴェルノワ・ド・サン＝ジョルジュ、劇作家（+ 1875年）"
}
{
  "type": "character",
  "character_id": 0,
  "message": "今日は何の日か知ってる？今日はジュール＝アンリ・ヴェルノワ・ド・サン＝ジョルジュさんの誕生日なのよ！",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "え？ジュール＝アンリ・ヴェルノワ・ド・サン＝ジョルジュって何それ何それ？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "ジュール＝アンリ・ヴェルノワ・ド・サン＝ジョルジュは、1799年に生まれたフランスの劇作家で、オペラやバレエの台本作家でもあったんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "えー、すごいね！劇作家って何をする人なの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "劇作家とは、演劇の上演のために戯曲を書く人のことを指すんだよ。古代ギリシャの劇作家たちは最も古い劇作家として知られているんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "ほえー、それならサン＝ジョルジュさんもすごい人なんだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうなの！サン＝ジョルジュさんは、70本以上の作品を残していて、その中にはオペラ『美しきパースの娘』やバレエ『ジゼル』の台本も含まれているんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わあ、それなら、すごく忙しかったんだね！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうだね。それに加えて、彼は1829年にオペラ＝コミック座の管理者となり、グランド・オペラ形式の台本も執筆したんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "ほえー、それならサン＝ジョルジュさんは本当にすごい人だったんだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうなの。サン＝ジョルジュさんは1875年にパリで亡くなったけど、彼の作品は今でも多くの人々に愛されているんだよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわん、それならサン＝ジョルジュさん、すごい人だったんだね！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それでは、次のトピックに移るよ！みなさん、お楽しみに！",
  "expression": "happy",
  "gesture": "wave hand"
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
  "message": "さてさて、次に紹介する出来事は、ちょっと怖いけど、すごく興味深いものよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "え？何それ何それ？怖いのはちょっと…。",
  "expression": "scared",
  "gesture": "shake head"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "（フィクションのできごと）1987年 - ピート・タイラーが交通事故死。娘ローズが歴史を書き換えたため、歴史を修正する怪物リーパーが出現し宇宙消滅の危機。（ドラマ『ドクター・フー』）"
}
{
  "type": "character",
  "character_id": 0,
  "message": "実は1987年の今日、あるドラマの世界で大事件が起こったの。それは…『ドクター・フー』の中で、ピート・タイラーが交通事故死した日なの。",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "ドクター・フー？それって何？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "\"ドクター・フー\"っていうのは、イギリスBBCで放映されているSFテレビドラマシリーズのことなんだよ。主人公のドクターと仲間たちが時空を自由に行き来し、外敵侵略やタイムパラドックスを防ぐために冒険するストーリーなんだ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "へー、時空を自由に行き来するなんて、すごいね！でも、ピート・タイラーって誰？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "ピート・タイラーは、ドクターの仲間であるローズの父親なんだよ。でも彼は交通事故で亡くなっちゃったんだ…。それが1987年の今日の出来事なんだけど、その後の展開がすごいの！",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "え？どうすごいの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "ローズが歴史を書き換えて父親を救おうとしたんだけど、それが原因で歴史を修正しようとする怪物リーパーが出現しちゃって、宇宙消滅の危機が起こっちゃったんだよ。",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "えー！それって大変じゃない？でも、ドクターたちはどうやってその危機を乗り越えたの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それはね、ドクターと仲間たちの機転と勇気で…でも、それはまた別のお話。今日はこのくらいにしておこうかな。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "うーん、でももっと知りたいなー。",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうだね、また次の機会に詳しく話すことにしよう。さて、次の出来事は何かな？",
  "expression": "happy",
  "gesture": "thinking pose"
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
  "message": "さて、次に紹介するのは、またまた誕生日のお祝いだよ。でも、ちょっと変わった誕生日だよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "え？どういうこと？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "（誕生日（フィクション））生年不明 - アリサ・ミハイロヴナ・九条、ライトノベル・漫画・アニメ『時々ボソッとロシア語でデレる隣のアーリャさん』のヒロイン"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それはね、今日はライトノベル・漫画・アニメ『時々ボソッとロシア語でデレる隣のアーリャさん』のヒロイン、アリサ・ミハイロヴナ・九条の誕生日なんだよ！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 1,
  "message": "おお！それはすごい！アーリャさんって、どんなキャラクターなの？",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "アーリャさんはね、ロシア人の父と日本人の母を持つハーフ女子高生で、征嶺学園の編入試験に合格して学年トップの成績を持つすごい子なんだよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わー、すごいね！でも、なんでロシア語でボソッとデレるの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それはね、アーリャさんはロシア語が分かるけど、主人公の政近にはそのことが知られていないんだよ。だから、時々ロシア語でつぶやくんだよ。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "なるほどね！それなら私もロシア語でデレることができるかな？",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それはちょっと難しいかもね（笑）。でも、アーリャさんの声優は上坂すみれさんが担当しているから、彼女の演技を見て勉強するといいかもよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "うん、それなら頑張ってみるね！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それが良いと思うよ！というわけで、アリサ・ミハイロヴナ・九条さん、お誕生日おめでとう！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 1,
  "message": "おめでとう！これからも素敵なキャラクターとして活躍してほしいね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうだね。これで今日のできごとの紹介は終わりだよ。でも、まだまだ配信は続くからね！次のコーナーもお楽しみに！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "hide",
  "position": "caption",
  "text": null
}
```

# 出力例（仮想ディベート）

```json
{
  "type": "character",
  "character_id": 0,
  "message": "ぴょこぴょこ星からこんにちは、永愛レイです！今日は特別なコーナー、「フィクション討論会」をお送りします！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわんわーお！犬山ボケ子だワン！一緒に楽しもうね！",
  "expression": "happy",
  "gesture": "wave hand"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：地球上に突如として、人間の言葉を理解し話すことができるペンギンが現れた。彼らは自分たちの生活環境を改善するために人間社会に参加したいと願っている。"
}
{
  "type": "character",
  "character_id": 0,
  "message": "今回の討論のテーマは、突如として人間の言葉を話すペンギンたちが現れ、彼らが人間社会に参加したいと願っているという設定です。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "何それ何それ？ペンギンが話すの？それってペットにできるの？",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：地球上に突如として、人間の言葉を理解し話すことができるペンギンが現れた。彼らは自分たちの生活環境を改善するために人間社会に参加したいと願っている。\nお題：ペンギンたちを人間社会に参加させるべきか否か"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そう、ペンギンが話すんだよ。でも、ペットではなく、彼らは人間と同等に社会に参加したいんだって。だから、今回のお題は「ペンギンたちを人間社会に参加させるべきか否か」なんだ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "ほほー、それは面白そうだワン！でも、ペンギンが人間社会に入ると、色々問題が起きそうだなぁ…",
  "expression": "thinking pose",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "私は賛成派だよ。ペンギンたちが人間のように社会に参加することで、新たな視点やアイデアが生まれるかもしれない。それに、彼らが自分たちの生活環境を改善したいという意志を尊重すべきだと思う。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "うーん、でもボケ子は反対だワン。ペンギンたちは寒い場所が好きだから、人間社会に合わせて暮らすとストレスを感じるかもしれない。それに、ペンギンが人間社会に入ると、魚が減るかもしれないワン！",
  "expression": "angry",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それは確かに問題だね。でも、人間社会がペンギンたちを受け入れることで、新たな技術やアイデアが生まれるかもしれないよ。たとえば、ペンギン用の冷房システムや、魚を効率的に生産する方法などが開発されるかもしれない。",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "type": "character",
  "character_id": 1,
  "message": "そうかもしれないけど、それでもボケ子はペンギンたちが自然の中で楽しく過ごす方がいいと思うワン！",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "うーん、それも一理あるね。でも、最終的にはペンギンたち自身がどうしたいか、それが一番大切なんじゃないかな。",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "そうだね、ペンギンたちの意見を尊重するのが一番だワン！",
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
  "message": "それで、次の討論会のお題は…",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "さてさて、次のお題に移りましょう！",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：2045年、科学者たちはタイムマシンを発明し、過去への旅を可能にした。しかし、過去に介入することで歴史が変わる可能性がある。"
}
{
  "type": "character",
  "character_id": 0,
  "message": "2045年、科学者たちはタイムマシンを発明しました。それによって過去への旅が可能になったんですよ！",
  "expression": "surprised",
  "gesture": "wave hand"
}
{
  "type": "character",
  "character_id": 0,
  "message": "でも、過去に介入することで歴史が変わる可能性があるんですって！",
  "expression": "scared",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわん！それって、昔のおやつを食べに行けるってこと？",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：2045年、科学者たちはタイムマシンを発明し、過去への旅を可能にした。しかし、過去に介入することで歴史が変わる可能性がある。\nお題：タイムトラベルを一般市民に開放すべきか否か"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そういうことではなくて、ボケ子ちゃん。今回のお題は、「タイムトラベルを一般市民に開放すべきか否か」なんですよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "うーん、それはちょっと危険かも…。人間って、ついつい過去を変えたくなっちゃう生き物だもん。",
  "expression": "sad",
  "gesture": "shake head"
}
{
  "type": "character",
  "character_id": 0,
  "message": "でも、タイムトラベルが可能になれば、歴史を学ぶ新たな方法が生まれるかもしれませんよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "でもでも、それって過去の人に迷惑かけちゃうかも…。昔のわたしに会ったら、きっとビックリしちゃうもん！",
  "expression": "surprised",
  "gesture": "shake head"
}
{
  "type": "character",
  "character_id": 0,
  "message": "それは確かに…。でも、きっとルールを作って、歴史を変えないようにするんじゃないかな？",
  "expression": "happy",
  "gesture": "thinking pose"
}
{
  "type": "character",
  "character_id": 1,
  "message": "そうかなー…。でも、わたしはやっぱり反対だわん！",
  "expression": "angry",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "うーん、なるほどね。私は賛成派だけど、ボケ子ちゃんの意見も分かるよ。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "というわけで、タイムトラベルを一般市民に開放すべきか否か、結論は…出ませんでした！",
  "expression": "surprised",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 1,
  "message": "わんわん、それはそれで面白い結果だね！",
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
  "message": "そうだね。さて、次のお題に進む前に、ちょっと一息つきましょうか。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "さて、我々の最後のお題に移りましょう！",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：地球外生命体が存在すると確定し、彼らは地球の食物を美味しいと感じるが、彼らが食べると人間にとっての食物が減る可能性がある。"
}
{
  "type": "character",
  "character_id": 0,
  "message": "設定はこうです。地球外生命体が存在することが確定し、彼らは地球の食物を美味しいと感じています。ただし、彼らが食べると人間にとっての食物が減る可能性があるんだって。",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "telop",
  "action": "show",
  "position": "caption",
  "text": "設定：地球外生命体が存在すると確定し、彼らは地球の食物を美味しいと感じるが、彼らが食べると人間にとっての食物が減る可能性がある。\nお題：地球外生命体に地球の食物を提供すべきか否か"
}
{
  "type": "character",
  "character_id": 0,
  "message": "今回のお題は、「地球外生命体に地球の食物を提供すべきか否か」です。",
  "expression": "default",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "私、永愛レイは賛成派です！",
  "expression": "happy",
  "gesture": "peace sign"
}
{
  "type": "character",
  "character_id": 0,
  "message": "私たちは宇宙の一部ですし、宇宙の仲間たちと共有することは素晴らしいことだと思います。それに、彼らが何を美味しいと感じるのか、それが新たな料理の発見につながるかもしれませんよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "ボケ子は反対だわん！",
  "expression": "angry",
  "gesture": "shake head"
}
{
  "type": "character",
  "character_id": 1,
  "message": "地球の食物が減ったら、ボケ子の大好きなピザがなくなっちゃうかもしれないわん！それは、それは、もう最悪だわん！",
  "expression": "sad",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "でも、ボケ子、考えてみて。地球外生命体がピザを美味しいと感じたら、宇宙ピザが誕生するかもしれないよ！",
  "expression": "happy",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 1,
  "message": "宇宙ピザ？それはそれで面白そうだわん！でも、それでも、ボケ子のピザがなくなるのは嫌だわん！",
  "expression": "surprised",
  "gesture": "none"
}
{
  "type": "character",
  "character_id": 0,
  "message": "そうね、これは難しい問題だけど、何か共通の解決策を見つけられるといいね。",
  "expression": "default",
  "gesture": "thinking pose"
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
  "message": "というわけで、今回のフィクション討論会はここまで！皆さん、いかがでしたか？私たちの討論はあくまでエンターテイメントですから、真剣に考えすぎずに楽しんでいただければと思います。",
  "expression": "happy",
  "gesture": "wave hand"
}
```

テロップが長いケースもあるね。GPT-3.5 に「テレビ番組のテロップ風に要約してください」みたいに要約してもらうのがいいかも？
