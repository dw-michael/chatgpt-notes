[« 寸劇クイズ](./03_random_skit.md)

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

今回はちゃんとゴールに着いた！使ったステップ数を言う指示を追加すれば視聴者も楽しく一緒に競争できるのでは？
