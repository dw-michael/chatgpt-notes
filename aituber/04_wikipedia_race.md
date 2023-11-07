[« 寸劇クイズ](./03_random_skit.md) | [テロップアクション »](./05_telop.md)

# 概要

Wikipedia レースとは、ランダムに選ばれたスタート記事から、リンクを辿るだけでランダムに選ばれたゴール記事まで最短距離で辿りつけようとする競争

視聴者と Wikipedia レースで競争するボットを書いてみた

# 出力例（ルート決め：GPT-3.5）

```json
{
  "character_id": 0,
  "message": "ぴょんぴょん、皆さんこんにちは！永愛レイです！今日は特別なコーナーをお届けしようと思います。その名も「Wikipediaレース」！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "Wikipediaレースとは、ランダムに選ばれたスタート記事から、記事内のリンクだけを辿って、ランダムに選ばれたゴール記事まで辿り着く競争なんです。最短でゴールにたどり着いた人の勝ち！ただし、カテゴリページと曖昧さ回避ページの使用は禁止ですよ。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今回のスタート記事は、「深井瞬」さん。テレビ新広島のアナウンサーで、東京都生まれ、埼玉育ちなんですって。そして、ゴール記事は、「林修のニッポンドリル」。これはフジテレビ系列で2018年から放送されていた番組ですね。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "それでは、レーススタート！",
  "expression": "surprised",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "最初に選んだリンクは「バラエティ番組」です。なぜなら、林修のニッポンドリルはバラエティ番組だからです。バラエティ番組は、色々なエンターテイメント要素を組み合わせたテレビ番組のことを指すんですよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に選んだのは「邦ちゃんのやまだかつてないテレビ」。これもバラエティ番組の一つですね。皆さん、覚えていますか？この番組、とっても面白かったですよね！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、次に選んだのは「折笠愛」さん。彼女は声優さんで、たくさんのアニメキャラクターを演じています。実はこの選択、ゴール記事の「林修」さんに近づくための戦略なんですよ。",
  "expression": "happy",
  "gesture": "thinking pose",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に選んだのは「めぐり逢えたら」。これは1993年のアメリカ映画で、ロマンチックなストーリーが描かれています。林修のニッポンドリルというバラエティ番組に関連するリンクを選びました。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に選んだのは「フジテレビジョン」です。林修のニッポンドリルはフジテレビで放送されていたからです。フジテレビは、日本の大手テレビ局の一つで、多くの人気番組を制作していますよね。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「松竹」を選びました。松竹は、映画や演劇の制作、興行、配給を手掛ける企業です。バラエティ番組とも関連が深いですね。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に、「新宿昭和館」を選びました。これは、かつて東京都新宿区三丁目にあった任侠映画専門の名画座で、今はもう存在していません。でも、その歴史はとても興味深いですよ。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「新宿駅」を選びました。新宿駅は、日本で最も利用者数が多い駅の一つで、多くの路線が交差しています。新宿駅からは、色々な場所にアクセスすることができますよね。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に、「新宿」を選びました。新宿は、新宿駅周辺の通称地名で、多くの商業施設やオフィスビルが立ち並んでいます。新宿の記事から新宿区の記事へと進むことにしました。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "最後に、「新宿区役所」を選びました。新宿区役所は新宿に関連する場所なので、ゴール記事に近づける可能性があると思ったからです。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "しかし、残念ながら、番組の尺の都合で、ここで時間切れです。ゴールには辿り着けませんでした。でも、次回に向けて、もっと効率的なルートを考えてみますね！",
  "expression": "sad",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "皆さんはどうでしたか？ゴールに辿り着けましたか？それとも、私と同じように途中で時間切れになってしまいましたか？ぜひコメントで教えてくださいね！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "それでは、今日の放送はここまで。次回も、楽しいWikipediaレースをお届けしますので、お楽しみに！それでは、またね〜！ぴょんぴょん！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
```

キャラクターのセリフは悪くないが、ルートがあまり頭良くないね（なぜ新宿？）

ルート決めは GPT-3.5 に任せてるけど GPT-4 にした方がいいかも？（コストが膨大になるけど）

# 出力例２（ルート決め GPT-3.5）

```json
{
  "character_id": 0,
  "message": "みなさん、こんにちは！永愛レイです！今日はとっても楽しいコーナーを持ってきましたよ！その名も「Wikipediaレース」！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "このWikipediaレースっていうのは、ランダムに選ばれたWikipediaの記事からスタートして、記事内のリンクだけを辿って、またランダムに選ばれたゴールの記事まで辿り着くという競争なんです。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "ただし、カテゴリページと曖昧さ回避ページの使用は禁止ですよ！最短ルートでゴールに辿り着いた人が勝ちになります！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今回のスタート記事は「TOKYOラッシュアワー」！そして、ゴール記事は「おどるポンポコリン」です！",
  "expression": "surprised",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "みなさんも一緒にこのレースに参加してみませんか？一緒にゴールを目指しましょう！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "それでは、レーススタートです！",
  "expression": "surprised",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "まずは「おかえりなさ〜い」の記事に移動します。このリンクを選んだ理由は、ゴール記事に近づくためには、このリンクを選ぶことができるからなんです！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に「Live News イット!」の記事に移動します。このリンクを選んだ理由は、B.B.クィーンズや音楽に関連する記事を探す必要があるからです。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "みなさん、どうですか？順調に進んでいますか？",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に「フジテレビジョン」の記事に移動します。ゴール記事はフジテレビから発売されたシングルなので、ここからは一気に近づけるはずです！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「お台場みんなの夢大陸」の記事に移動します。フジテレビジョンと関連しているリンクを選ぶことで、ゴール記事に近づける可能性が高いと考えました。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に辿るリンクは「ちびまる子ちゃん」です。このリンクを選ぶ理由は、ゴール記事には「ちびまる子ちゃん」のエンディングテーマとして使われた曲が含まれているからです。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "最後に「BMG JAPAN」の記事に移動します。『おどるポンポコリン』のシングル情報を含むB.B.クィーンズの記事に進むためです。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、ついにゴールの「おどるポンポコリン」の記事に到着！みなさん、どうでしたか？無事にゴールできましたか？",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今日のWikipediaレースはここまで！みなさんの結果をコメントで教えてくださいね！それでは、また次回をお楽しみに！バイバイ！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
```

ルート決めのプロンプトを少し調整した。今回はちゃんとゴールに着いた！使ったステップ数を言う指示を追加すれば視聴者も楽しく一緒に競争できるのでは？

# 出力例３（プロンプト決め GPT-3.5）

```json
{
  "character_id": 0,
  "message": "ぴょこんぴょこん、みんな〜！永愛レイだよっ！今日も元気に地球観察隊として活動するよ〜！今日は特別なコーナーを用意していてね、それが「Wikipediaレース」だよ！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "Wikipediaレースって何？って思う人もいるかもしれないけど、これはね、ランダムに選ばれたWikipediaの記事からスタートして、記事内のリンクだけを辿って、またランダムに選ばれたゴールの記事まで辿り着く競争なんだよ！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "でもね、カテゴリページと曖昧さ回避ページの使用は禁止だよ！それじゃあ、今回のスタート記事とゴール記事を発表するね！",
  "expression": "surprised",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "スタート記事は「千葉県立勝浦若潮高等学校」！これは千葉県勝浦市新官に所在する高等学校の記事だよ。そして、ゴール記事は「偕楽園駅」！これは茨城県水戸市常磐町一丁目にある東日本旅客鉄道（JR東日本）常磐線の駅の記事だよ！",
  "expression": "happy",
  "gesture": "peace sign",
  "type": "character"
}
{
  "character_id": 0,
  "message": "さあ、みんなも一緒に挑戦してみてね！それじゃあ、レース、スタート！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "さて、最初に辿るリンクは「2005年」ね。偕楽園駅は臨時駅で特定の時期に営業しているから、年代に関連するリンクを選んでみたんだよ！",
  "expression": "default",
  "gesture": "thinking pose",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に辿るリンクは「インターネットサービスプロバイダ」だよ。偕楽園駅に近づくためには、鉄道に関連する話題がいいと思ってね。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "みんな、ついてきてる？次は「東北電力フロンティア」だよ！偕楽園駅は偕楽園の梅まつりの時期に営業しているから、それに関連しそうなリンクを選んでみたんだよ。",
  "expression": "happy",
  "gesture": "thinking pose",
  "type": "character"
}
{
  "character_id": 0,
  "message": "その次は「東北電力」ね。東北電力フロンティアは東北電力の子会社だから、関連するリンクを選んでみたんだよ。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「相馬共同火力発電」へ！偕楽園駅は常磐線の駅だから、常磐線に関連するリンクを選んでみるとゴールに近づけるかもしれないよね！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次は「常磐共同火力」だよ！相馬共同火力発電と偕楽園駅はどちらも鉄道関連の記事だから、鉄道に関連するリンクを選ぶとゴールに近づけるかも！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次のリンクは「常磐炭田」だよ！常磐共同火力株式会社は常磐地区の炭鉱会社の共同出資で設立されたから、常磐炭田に関連するリンクを選んでみたんだよ。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "その次は「富岡町」ね。常磐炭田の地域や歴史に関連するリンクを選ぶのが効果的だと思って選んだんだよ！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「富岡駅」だよ！富岡町と偕楽園駅は同じ常磐線にあるから、常磐線に関連するリンクを選んだんだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次は「双葉郡」ね。偕楽園駅に近づくためには、偕楽園駅に関連するリンクを選ぶといいと思って選んだんだよ！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「水戸市」！水戸市は茨城県の主要な都市で、偕楽園駅も茨城県にあるから、このリンクを選んだんだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次のリンクは「水戸市民球場」だよ。水戸市と偕楽園駅は同じ水戸市にあるから、水戸市の記事から偕楽園駅の記事に辿り着くことができると思って選んだんだよ！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、最後に「水戸駅」ね！偕楽園駅に近づくためには、常磐線の駅に関連するリンクを選ぶ必要があるから、水戸駅を選んだんだよ！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、ついにゴールの「偕楽園駅」に到着！全部で14ステップだったよ！みんなはどうだったかな？成功した人もいるかな？",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今日も一緒に楽しんでくれてありがとう！また次回も楽しいことをたくさん用意して待ってるから、また遊びに来てね！それじゃあ、バイバイ！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
```

ステップの上限を少し上げてステップ数を最後に言うように指示を追加

リンクを選んだ根拠が弱い時があるが、それはルート決めの GPT-3.5 のせいでもある（ルート決めと同時に根拠を出力させている）

費用： $0.26

# ルート決め工夫（GPT-3.5 と GPT-4 の比較）

## GPT-3.5

```
Start: 角田市立北角田中学校
Goal: 有村昆
Limit: 15 steps

1. Page: 中学校; Reason: 有村昆はラジオパーソナリティであり、この中学校の記事には学校経営の情報があるため、次は「学校経営」の記事に進むことで有村昆に関連する情報が得られるかもしれません。
2. Page: アメリカ合衆国; Reason: 中学校の記事には学校経営の情報があるため、次は「学校経営」の記事に進むことでゴールに近づけると思います。
3. Page: アメリカの環境と環境政策; Reason: アメリカ合衆国の環境と環境政策の記事には、アメリカの社会問題や政策に関する情報がある可能性があります。有村昆は映画コメンテーターとしても知られているので、映画やエンターテイメントと環境問題の関連性を考えると、この記事に進むことでゴールに近づけるかもしれません。
4. Page: アメリカの軍需経済と軍事政策; Reason: アメリカの環境と環境政策の記事には、アメリカの社会問題や政策に関する情報がある可能性があります。有村昆は映画コメンテーターでもあり、アメリカの映画産業にも関わっているので、アメリカの社会問題や政策に関連する情報を探すことでゴールに近づけるかもしれません。
5. Page: 1968年; Reason: アメリカの軍需経済と軍事政策の記事にはアメリカの軍事に関する情報がある可能性があり、有村昆はアメリカの軍事についての情報を提供しているかもしれないため、次は「アメリカの軍事」の記事に進むことでゴールに近づけると思います。
6. Page: 映画監督; Reason: 有村昆は映画コメンテーターでもあるので、映画監督の記事に進むことでゴールに近づけると思います。
7. Page: 監督; Reason: 映画監督の記事に進むことで、有村昆の映画関連の情報を得ることができ、ゴールに近づける可能性があると思います。
8. Page: 監督代行; Reason: 監督の記事に進むことで、有村昆の映画関連の情報を得ることができ、ゴールに近づける可能性があると思います。
9. Page: 藤本定義; Reason: 監督代行の記事には、有村昆の映画関連の情報がある可能性があり、ゴールに近づける可能性があると思います。
10. Page: プロ野球監督; Reason: 藤本定義はプロ野球監督であり、藤本定義の記事には有村昆に関連する情報がある可能性があるため、次は「藤本定義」の記事に進むことでゴールに近づけると思います。
11. Page: 野球選手; Reason: プロ野球監督の記事に進むことで、有村昆のプロ野球関連の情報を得ることができ、ゴールに近づける可能性があると思います
12. Page: 日本; Reason: 有村昆は日本のラジオパーソナリティなので、次は「日本」の記事に進むことで有村昆に関連する情報を得ることができ、ゴールに近づける可能性があると思います。
13. Page: 経済成長; Reason: 「日本」の記事に進むことで、有村昆に関連する情報を得ることができる可能性があり、ゴールに近づけると思います
14. Page: 投資; Reason: 経済成長に関連するリンクを選びます。経済成長の要素として、投資が重要な要素とされていますので、次は「投資」の記事に進むことで経済成長に関連する情報を得ることができ、ゴールに近づける可能性があります。
15. Page: 投資家; Reason: 投資家の記事に進むことで、投資に関する情報を得ることができ、有村昆の活動に関連する可能性があるため
```

やはり選んだリンクも理由づけも訳がわからない。適当なことを言っているように見える。

費用： $0.05

## GPT-4

```
Start: 角田市立北角田中学校
Goal: 有村昆
Limit: 15 steps

1. Page: 宮城県; Reason: 有村昆は日本のラジオパーソナリティで、宮城県は日本の一部である。この関連性を利用して、次に「宮城県」のリンクを選ぶ。
2. Page: オールニッポン・ニュースネットワーク; Reason: 有村昆はラジオパーソナリティであり、そのためメディアや放送に関連するリンクを選ぶのが良さそうです。その中で「オールニッポン・ニュースネットワーク」は全国的なニュースネットワークであり、有村昆が出演する可能性が高いと考えられます。
3. Page: AbemaTV; Reason: 有村昆はラジオパーソナリティであり、テレビやラジオ放送に関連するリンクを選ぶのが良さそうです。その中でも「AbemaTV」は、インターネットテレビ局であり、様々な番組を配信しているため、有村昆が出演している可能性があると考えました。
4. Page: ABEMA; Reason: 有村昆は映画コメンテーターでもあり、AbemaTVは映画などのエンターテイメント番組を多く放送している。そのため、AbemaTVの記事から有村昆に関連する情報やリンクが見つかる可能性がある。
5. Page: ニュース専門放送局; Reason: 有村昆はラジオパーソナリティであり、そのためメディアや放送に関連するリンクを選ぶのが良さそうです。その中でも、「ニュース専門放送局」はニュースや情報を発信する場所であり、有村昆が活動している分野と直接関連しています。また、彼は映画コメンテーターでもあるため、映画やエンターテイメントに関連する情報が含まれている可能性もあります。このリンクを選ぶことで、有村昆についての情報に近づけると考えます。
6. Page: 日本放送協会; Reason: 有村昆はラジオパーソナリティであり、ラジオは放送の一部です。そのため、放送に関連するリンクを選ぶと有村昆に近づける可能性があると考えます。その中でも「日本放送協会」は日本の公共放送であり、ラジオ放送も行っているため、有村昆との関連性があると考えられます。
7. Page: らじるらじる; Reason: 有村昆はラジオパーソナリティで、NHKとしては「らじるらじる」が該当する。このリンクを選ぶことで、有村昆と直接的に関連する記事にたどり着く可能性があると考えられる。
8. Page: NHKネットラジオ らじる★らじる; Reason: 有村昆はラジオパーソナリティであり、NHKのネットラジオ「らじる★らじる」は彼の職業と直接関連がある。このリンクを選ぶことで、有村昆についての情報が含まれている可能性が高い記事に辿り着く可能性がある。
9. Page: NHKラジオ第1放送; Reason: 有村昆はラジオパーソナリティであり、そのためラジオに関連するリンクを選ぶのが良さそうです。その中でも、「NHKラジオ第1放送」はNHKの代表的なラジオ放送であり、有村昆が出演する可能性が高いと思われます。したがって、このリンクを選ぶことで有村昆に近づけると考えられます。
10. Page: NHKのど自慢; Reason: 有村昆はラジオパーソナリティであるため、彼が出演した可能性のある番組についての記事を選ぶと彼につながる可能性がある。そのため、NHKのラジオ番組である「NHKのど自慢」の記事を選ぶ。
11. Page: ニッポン放送; Reason: 有村昆はラジオパーソナリティであり、多くの放送関連の記事を経由してきました。その中で「ニッポン放送」は大きなラジオ放送局で、有村昆が関わる可能性があると思われます。
12. Page: デジタルラジオ; Reason: 有村昆はラジオパーソナリティであり、そのためラジオに関連するリンクを選ぶのが良さそうです。その中でも「デジタルラジオ」は最新のラジオ放送技術に関連しており、有村昆が関与する可能性があるため選びます。
13. Page: NHKワールド・ラジオ日本; Reason: 有村昆はラジオパーソナリティであるため、ラジオ放送に関連するリンクを選んだ。その中でも「NHKワールド・ラジオ日本」はNHKの国際放送であり、有村昆が出演する可能性があると考えた。
14. Page: ラジオ番組; Reason: 有村昆はラジオパーソナリティで、ラジオ番組に関連性があるはず。そのため、ラジオ番組についての記事に進むと、有村昆についての情報が出てくる可能性がある。
15. Page: ラジオパーソナリティ; Reason: 有村昆はラジオパーソナリティであるため、ラジオパーソナリティについての記事に進むと、彼についての情報が得られる可能性が高いです。
```

制限ステップ数以内にゴールできなかったけど、理由づけがちゃんとしていて惜しいところまできた。

費用： $1.18 （前処理にしては高いし遅い）

# 出力例（ルート決め：GPT-4）

```json
{
  "character_id": 0,
  "message": "ぴょこん！永愛レイ、地球観察隊の一員で、ぴょこぴょこ星からやってきたAI VTuberだよ！今日は特別なコーナーをお届けするよ！",
  "expression": "default",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "その名も「Wikipediaレース」！これは、ランダムに選ばれたWikipediaの記事からスタートして、記事内のリンクだけを辿って、またランダムに選ばれたゴール記事まで辿りつけるか競う、知識と直感のレースなんだ！",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "ルールはシンプル！カテゴリページや曖昧さ回避ページは使えないよ。そして、最短ルートでゴールに辿り着いた人が勝者！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今日のスタート記事は「天嶽寺」。これは埼玉県越谷市にある浄土宗の寺院なんだって。そして、ゴール記事は「おしい刑事」。これは藤崎翔による連作短編ミステリ小説集なんだよ。",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "さあ、みんなも一緒に挑戦してみてね！私のルートを参考に、もしくは自分なりのルートを探してみて！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
{
  "character_id": 0,
  "message": "それでは、レーススタート！まずは「天嶽寺」から…",
  "expression": "surprised",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "「おしい刑事」はミステリ小説集だから、推理要素が含まれているかもしれないよね。だから最初に選んだのは「曲亭馬琴」。これは江戸時代の戯作家で、物語をつくる人だから関連しそうだよね！",
  "expression": "happy",
  "gesture": "thinking pose",
  "type": "character"
}
{
  "character_id": 0,
  "message": "次に「日本文学」を選んだのは、「おしい刑事」も日本の文学の一部だからだよ。そして、「小説家」、「小説」、「スパイ小説」を選んだのは、小説のジャンルや作者について知ることで、ゴールに近づけると思ったからだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "ここで「アガサ・クリスティ」を選んだのは、彼女が推理小説の大家だからだよ。そして、「推理小説」、「日本ミステリー文学大賞新人賞」、「推理小説の賞」を選んだのは、これらがミステリ小説と直接関連しているからだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "そして、「新潮社」、「新潮ミステリー大賞」、「湊かなえ」を選んだのは、これらが出版やミステリ小説と関連しているからだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "最後に、「ポプラ社」、「ポプラ文庫」、「ポプラ文庫ピュアフル」を選んだのは、「おしい刑事」がポプラ社から出版されているからだよ。",
  "expression": "happy",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "でも、残念ながらゴールには辿り着けなかったんだ…。番組の尺が足りなくて、時間内にゴールに到達することができなかったんだよね。",
  "expression": "sad",
  "gesture": "shake head",
  "type": "character"
}
{
  "character_id": 0,
  "message": "今回は15ステップで挑戦を終えたよ。みんなはどうだったかな？成功した人はいるかな？コメントで教えてね！",
  "expression": "default",
  "gesture": "none",
  "type": "character"
}
{
  "character_id": 0,
  "message": "それでは、今日の「Wikipediaレース」はここまで！また次回も一緒に楽しみながら知識を深めていこうね！それでは、バイバイ！",
  "expression": "happy",
  "gesture": "wave hand",
  "type": "character"
}
```

視聴者がついていけないくらい早い進行だけど、ルートの理由づけはちゃんとしている。

だたしめっちゃ時間かかったし、$0.83 かかった。
