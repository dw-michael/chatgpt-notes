[« 詳しいキャラ設定 v2 »](./12_detailed_characters.md)

# 概要

Anthropic 社が提供する Claude という LLM が自然な会話・フィクション系に長けていると聞いたので使ってみた。

そのために AITuber の OpenAI 特化だった LLM API を一般化し、両方の LLM に対応するサブクラスを書いた。

OpenAI と違って JSON 出力特化のモデルがないので、崩れた出力の対応処理も追加。

# 出力例 ①

```markdown
# intro

円溜しらべ: みなさん、こんにちは！
円溜しらべ: V 高等学校配信部の部長、円溜しらべです！
クリメネ: こんにちは…クリメネです
クリメネ: よろしくお願いします…
娯楽あたり: 娯楽あたりだよ
娯楽あたり: よろしく
円溜しらべ: クーちゃん、素直でいいですね！
クリメネ: しらべ先輩、ありがとうございます…！
円溜しらべ: たりちゃんも堂々としていて素晴らしいです！
娯楽あたり: しらべちゃんにそう言ってもらえるとうれしいね
娯楽あたり: クーちゃんも可愛いね
クリメネ: え、そ、そんな…照れちゃうよ…
円溜しらべ: ところで、最近面白いことあった人いますかー？
娯楽あたり: ぼくはね、昨日ゲーセンで UFO キャッチャーやってたんだ
娯楽あたり: でも全然取れなくて…ついカッとなって台をバーンッ！って叩いちゃったの
娯楽あたり: そしたらなんと、隣の台から景品が落ちてきたんだよ！
娯楽あたり: びっくりだよね
円溜しらべ: えええッ！？
円溜しらべ: それは驚きですね！
クリメネ: 台を叩いたら隣から景品が…！？
クリメネ: すごいね…
円溜しらべ: でも、隣の台の人には申し訳ないですよねッ…！
娯楽あたり: そうなんだよね…ちょっと後ろめたかったよ…
円溜しらべ: みなさんも面白い体験があったら教えてくださいね！
円溜しらべ: それでは、今日の配信、よろしくお願いしまーす！
```

![](https://lohas.nicoseiga.jp/thumb/11431859i)

```markdown
# seiga_review

[TELOP: 隣の子が盛大に寝てた by jonsun (im11431859)]
白恋花しゃろん: うわぁ、この子すっごく気持ちよさそうに寝てるね！
白恋花しゃろん: アタシもこんな風に寝たいなぁ
黒緑鬼: ふむ、リクちゃんとかいう子らしいのう
黒緑鬼: 競泳水着を着とるところを見ると、水泳部の子なんじゃろうな
白恋花しゃろん: ねぇねぇこみー、リクちゃんのおっぱいすごくない？
白恋花しゃろん: こんなに大きくてプルンプルンだよ！
黒緑鬼: しゃろんは相変わらずおっぱいが大好きじゃのう
黒緑鬼: まぁ確かにリクちゃんはなかなかのものを持っとるが
白恋花しゃろん: jonsun さんが描いたリクちゃん、本当に幸せそうだよね
白恋花しゃろん: アタシもこんな風に寝たら、きっと素敵な夢が見られるんだろうなぁ
黒緑鬼: うむ、リクちゃんを見とると和むのう
黒緑鬼: jonsun さんはリクちゃんの魅力をよく表現しとるわい
```

![](https://lohas.nicoseiga.jp/thumb/11431820i)

```markdown
[TELOP: im11431820【流行りのレモンとヒシミラクル】]
[TELOP: 投稿者：はるとろ]
黒緑鬼: さて、次のイラストじゃな
黒緑鬼: おおっ！
黒緑鬼: これは酸っぱそうじゃのう！
白恋花しゃろん: ウマ娘のヒシミラクルちゃんがレモンを食べてる絵だね！
白恋花しゃろん: 顔がすっぱそうだよ！
黒緑鬼: レモンは酸っぱいからのう
黒緑鬼: わしも昔食べて顔がしかめっ面になったことがあるわい
白恋花しゃろん: こみーもレモン食べたことあるんだ！
白恋花しゃろん: アタシも食べてみたーい！
黒緑鬼: しゃろんにはまだ早いと思うぞ
黒緑鬼: それにしても、はるとろさんが描いたヒシミラクルの表情がとてもリアルじゃな
白恋花しゃろん: そうだね！
白恋花しゃろん: すっぱくて目が回っちゃってる感じが伝わってくるよ！
白恋花しゃろん: はるとろさんの絵、すごいね！
黒緑鬼: ウマ娘ファンの間でも話題になっとるようじゃな
黒緑鬼: 流行りのレモンを使った面白い発想じゃ
白恋花しゃろん: ヒシミラクルちゃんの新しい一面が見れた気がするよ！はるとろさんの絵の
白恋花しゃろん: 力だね！
```

![](https://lohas.nicoseiga.jp/thumb/11431609i)

```markdown
[TELOP: im11431609【悔い多き世界線の鳳翔さん】]
[TELOP: 投稿者：ツンイチ]
黒緑鬼: おおお！
黒緑鬼: これは艦これの鳳翔さんが ν ガンダムになっとるのう！
黒緑鬼: 艦娘とガンダムのコラボじゃな
白恋花しゃろん: わぁ、かっこいい！
白恋花しゃろん: 鳳翔さんがロボットになってるよ！
白恋花しゃろん: フィン・ファンネルがいっぱい飛んでるね！
黒緑鬼: ファンネルは遠隔操作の武器じゃな
黒緑鬼: ν ガンダムの代名詞的な装備じゃ
黒緑鬼: 鳳翔さんもファンネルで敵をやっつけるんじゃろうのう
白恋花しゃろん: ふふふ、鳳翔さんがロボットになって戦うのって面白いね！
白恋花しゃろん: ツンイチさんのアイデアが素晴らしいよ！
黒緑鬼: ほんまじゃのう
黒緑鬼: 艦これとガンダムという人気作品のコラボで、ファンにはたまらん作品じゃろうて
黒緑鬼: わしも艦これはよう知らんが、このイラストは迫力があっていいのう
白恋花しゃろん: そうだね！
白恋花しゃろん: 二つの世界が合わさって、新しい物語が生まれてるみたい！
白恋花しゃろん: ツンイチさんの創造力に拍手！
黒緑鬼: うむ
黒緑鬼: ほんならこのイラストの紹介はこれぐらいにしとくかのう
黒緑鬼: みんなも気になったら、ニコニコ静画でツンイチさんの作品をチェックしてみてくだされ〜

# daily_events

白恋花しゃろん: みなさん、こんにちは！
白恋花しゃろん: 今日は 2024 年 5 月 14 日ですね
娯楽あたり: そういえば、今日は 1888 年に明治唱歌第 1 集が発行された日なんだよね
[TELOP: 1888 年 5 月 14 日 - 明治唱歌第 1 集発行]
白恋花しゃろん: へぇ、明治唱歌って何だろう…？
白恋花しゃろん: クーちゃん、詳しく教えてくれる？
娯楽あたり: 明治唱歌は明治時代の小学校の音楽教育のための唱歌集なんだ
娯楽あたり: 1872 年の学制で小学校の教科に唱歌が定められたんだけど、
娯楽あたり: 当初はあまり普及しなかったんだよね
娯楽あたり: でも、1888 年頃から民間出版の唱歌集が出始めて、
娯楽あたり: 明治唱歌第 1 集もその一つなんだ
白恋花しゃろん: なるほどね…
白恋花しゃろん: 明治唱歌ってどんな曲が入ってるの？
娯楽あたり: 明治唱歌第 1 集には「窓をあける」とか「赤とんぼ」、「うみ」など、
娯楽あたり: 今でも親しまれてる曲が収録されてるんだ
白恋花しゃろん: あぁ、「赤とんぼ」は知ってるよ！
白恋花しゃろん: 優しくて懐かしい感じの歌だよね
娯楽あたり: そうそう
娯楽あたり: 明治唱歌は国民の道徳心や愛国心を育てるのが目的だったんだ
娯楽あたり: 明治時代の音楽教育や国民教化の一環として、重要な役割を果たしたんだよ
白恋花しゃろん: クーちゃんは明治唱歌についてよく知ってるんだね！
娯楽あたり: まぁね…
娯楽あたり: でも明治唱歌は日本の音楽教育の歴史の中で重要なんだよ
娯楽あたり: その後も唱歌教育は発展していって、1907 年には小学校の必須科目になったんだ
白恋花しゃろん: へぇ…
白恋花しゃろん: そういう歴史があったんだね
白恋花しゃろん: 勉強になったよ！
娯楽あたり: うん、今日は明治唱歌第 1 集発行の記念日だったね
娯楽あたり: みんなも童謡とかに親しんでみるといいかも！
白恋花しゃろん: そうだね！
白恋花しゃろん: 童謡って心が和むし、日本の文化も感じられるから面白いよね
クリメネ: あたりちゃん、今日 5 月 14 日に起こったことで他に何か面白いのあった？
娯楽あたり: そういえば、5 月 14 日って特撮ドラマの主人公の誕生日なんだよね
クリメネ: へぇ〜、どんな特撮ドラマなの？
[TELOP: ポリス × 戦士 ラブパトリーナ!]
娯楽あたり: 「ポリス × 戦士 ラブパトリーナ!」っていうんだ
娯楽あたり: 2020 年から 2021 年にかけてテレビ東京系列で放送されてた少女向けの
娯楽あたり: 特撮ドラマだよ
クリメネ: 主人公の子の誕生日が今日なんだね
クリメネ: 主人公ってどんな子なの？
[TELOP: 主人公：愛羽ツバサ]
娯楽あたり: 主人公は愛羽ツバサっていう女の子なんだけど、ツバサの母親が小説家の
娯楽あたり: 愛羽優って人で、「名探偵マグレ」シリーズを書いてるんだって
クリメネ: ふ〜ん…でも、ツバサちゃんの生年月日はプロフィールに書いてなかったんだよね〜
クリメネ: ちょっと残念だなぁ…
娯楽あたり: ま、生年不明ってことは、ツバサは何歳でも演じられるってことだからいいんじゃない？
娯楽あたり: これからもラブでパパッとタイホしてほしいね！
クリメネ: そうだね！
クリメネ: ツバサちゃん、お誕生日おめでとう！
クリメネ: これからも頑張ってね！
娯楽あたり: そして次の 5 月 14 日のできごとは...
[TELOP: 5 月 14 日のできごと]
クリメネ: うんうん、次は何かな...？
娯楽あたり: 小説『化物語』で阿良々木暦（あららぎ こよみ）と八九寺真宵（はちくじ まよい）が
娯楽あたり: 出会ったんだって
[TELOP: 小説『化物語』より]
クリメネ: ファンタジー小説の中の出来事なんだね...！
クリメネ: でも、5 月 14 日って何か関係あるのかな...？
娯楽あたり: 実は小説の中ではいつ出会ったのか正確な日付は書かれてないんだよね...
娯楽あたり: でも、5 月って新学期が始まる季節だから、クラスメイトとして出会うには
娯楽あたり: ぴったりの時期なんだよ
クリメネ: なるほど...！
クリメネ: 新学期に新しい出会いがあるのは、現実世界でも小説の中でも同じなんだね
娯楽あたり: そうそう
娯楽あたり: 小説の中では、主人公の暦くんが春休み中に吸血鬼に襲われて怪我をしたんだけど
娯楽あたり: ...
娯楽あたり: その怪我が異常に早く治ったことがきっかけで、いろんな不思議な出来事に
娯楽あたり: 巻き込まれていくんだ
クリメネ: え、吸血鬼!? こわいよ...
クリメネ: でも、怪我が早く治るのは良いことなのかな...？
娯楽あたり: そこから暦くんは、体重を奪われて 5kg しかないクラスメイトの女の子、
娯楽あたり: ひたぎを助けることになるんだ
クリメネ: 体重が 5kg!? そんなの絶対おかしいよね...
クリメネ: ひたぎさん、大丈夫なのかな...
娯楽あたり: ひたぎを助けるために、暦くんは委員長の翼や、怪異に詳しいメメさんたちの
娯楽あたり: 力を借りるんだ
娯楽あたり: みんなで力を合わせて、ひたぎの問題を解決していくお話なんだよ
クリメネ: みんなで協力し合うのは大事だよね
クリメネ: 怪異のこと、よくわかんないけど...きっと友達の力があれば何とかなるよね！
娯楽あたり: そうだね
娯楽あたり: ひたぎは最初は暦くんに毒舌だったみたいだけど、助けてもらったことで
娯楽あたり: 段々と打ち解けていくみたい
娯楽あたり: 新学期の出会いが、こんな大きな冒険のきっかけになるなんて面白いよね！
クリメネ: 新学期の出会いって、一生の友達になるかもしれないからワクワクするよね
クリメネ: 私たちも、これからどんな冒険が待ってるのかな...！
娯楽あたり: うん、私たちも新学期を迎えたばかりだし、これから楽しいことがいっぱい
娯楽あたり: ありそうだよね！
娯楽あたり: 今日は小説の中の出来事を見てきたけど、現実の新学期の出会いも大切に
娯楽あたり: していきたいな
クリメネ: そうだね、あたりちゃん！
クリメネ: 新しいクラスのみんなとも仲良くなれたらいいな...
クリメネ: これからの学校生活、がんばろうね！
娯楽あたり: うん、一緒にがんばろう、クーちゃん！
娯楽あたり: というわけで、今日は 5 月 14 日にまつわる小説の出来事を見てきました！
クリメネ: 新学期のドキドキわくわくな雰囲気を感じられたかな...？
クリメネ: 現実世界の新学期も、素敵な出会いがあるといいですね！
娯楽あたり: 今日のできごと紹介コーナーは以上です！
娯楽あたり: それじゃあまたね！

# ending

円溜しらべ: 今日のニコニコ倶楽部はいかがでしたか？
円溜しらべ: 娯楽あたりのゲーセンエピソードはびっくりしましたねー！
円溜しらべ: でも、隣の人には申し訳なかったそうなので、ちゃんと謝ったんでしょうかッ？
黒緑鬼: あの子は良い子じゃけど、ちょっと行動力がありすぎるのう
黒緑鬼: でも、あれで良い体験談ができたんじゃからよかったんじゃないかのー
円溜しらべ: そうですねー
円溜しらべ: ちょっとした失敗も、楽しい思い出になるものですッ！
円溜しらべ: それから、今日紹介された静画もすごかったですねー
黒緑鬼: ほんまじゃのー
黒緑鬼: あの ν ガンダムになった鳳翔（ほうしょう）さんかっこよかったのう
黒緑鬼: 二つの世界が混ざり合って、新しいストーリーが生まれとるんが面白いのー
円溜しらべ: 5 月は新しい出会いの季節ですからねー
円溜しらべ: 小説の中でも、暦（こよみ）くんとひたぎさんが出会って、冒険が始まるみたいですッ！
円溜しらべ: これからどんな物語が展開するのか、わたしもわくわくしちゃいますッ！
黒緑鬼: わしも楽しみじゃのー
黒緑鬼: それじゃあ、今日のニコニコ倶楽部はここまでじゃな
黒緑鬼: みんなも良い出会いがありますようにのー
黒緑鬼: それじゃあ、また来週ーッ！
円溜しらべ: 今日も見てくださってありがとうございましたッ！
円溜しらべ: 来週もお楽しみにーッ！
円溜しらべ: ニコニコ倶楽部、おしまいっ！
```

## 元の JSON

参考に（表情とかの情報もあるので）

```json
[
  {
    "name": "intro",
    "commands": [
      {
        "command": "Corner",
        "data": {
          "action": "start",
          "name": "イントロ"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "みなさん、こんにちは！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "V高等学校配信部の部長、円溜しらべです！",
          "readings": {
            "円溜しらべ": "えんためしらべ"
          },
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "こんにちは…クリメネです",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "よろしくお願いします…",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "娯楽あたりだよ",
          "readings": {
            "娯楽あたり": "ごらくあたり"
          },
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "よろしく",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "クーちゃん、素直でいいですね！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:2"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "しらべ先輩、ありがとうございます…！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "たりちゃんも堂々としていて素晴らしいです！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "しらべちゃんにそう言ってもらえるとうれしいね",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "クーちゃんも可愛いね",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:2"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "え、そ、そんな…照れちゃうよ…",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "ところで、最近面白いことあった人いますかー？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ぼくはね、昨日ゲーセンでUFOキャッチャーやってたんだ",
          "readings": {
            "UFOキャッチャー": "ユーフォーキャッチャー"
          },
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "でも全然取れなくて…ついカッとなって台をバーンッ！って叩いちゃったの",
          "readings": {},
          "facialExpression": "ふくれっ面",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そしたらなんと、隣の台から景品が落ちてきたんだよ！",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "びっくりだよね",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "えええッ！？",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "それは驚きですね！",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "台を叩いたら隣から景品が…！？",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "すごいね…",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "でも、隣の台の人には申し訳ないですよねッ…！",
          "readings": {},
          "facialExpression": "苦笑い",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そうなんだよね…ちょっと後ろめたかったよ…",
          "readings": {},
          "facialExpression": "引きつり笑顔",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "みなさんも面白い体験があったら教えてくださいね！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "それでは、今日の配信、よろしくお願いしまーす！",
          "readings": {},
          "facialExpression": "通常",
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
    ]
  },
  {
    "name": "seiga_review",
    "commands": [
      {
        "command": "Corner",
        "data": {
          "action": "start",
          "name": "静画紹介"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "title",
          "text": "隣の子が盛大に寝てた by jonsun (im11431859)"
        }
      },
      {
        "command": "Image",
        "data": {
          "action": "show",
          "format": "web",
          "image_url": "https://lohas.nicoseiga.jp/thumb/11431859i"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "うわぁ、この子すっごく気持ちよさそうに寝てるね！",
          "readings": {
            "すっごく": "スッゴク"
          },
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "アタシもこんな風に寝たいなぁ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ふむ、リクちゃんとかいう子らしいのう",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "競泳水着を着とるところを見ると、水泳部の子なんじゃろうな",
          "readings": {
            "競泳水着": "キョウエイミズギ"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ねぇねぇこみー、リクちゃんのおっぱいすごくない？",
          "readings": {},
          "facialExpression": "ウィンク",
          "facing": "character:1"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "こんなに大きくてプルンプルンだよ！",
          "readings": {
            "プルンプルン": "プルンプルン"
          },
          "facialExpression": "ドヤ顔",
          "facing": "character:1"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "しゃろんは相変わらずおっぱいが大好きじゃのう",
          "readings": {
            "相変わらず": "アイカワラズ"
          },
          "facialExpression": "苦笑い",
          "facing": "character:3"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "まぁ確かにリクちゃんはなかなかのものを持っとるが",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:3"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "jonsunさんが描いたリクちゃん、本当に幸せそうだよね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "アタシもこんな風に寝たら、きっと素敵な夢が見られるんだろうなぁ",
          "readings": {},
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "うむ、リクちゃんを見とると和むのう",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "jonsunさんはリクちゃんの魅力をよく表現しとるわい",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "title",
          "text": null
        }
      },
      {
        "command": "Pause",
        "data": {
          "duration": 2
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "title",
          "text": "im11431820【流行りのレモンとヒシミラクル】"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "caption",
          "text": "投稿者：はるとろ"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "さて、次のイラストじゃな",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "おおっ！",
          "readings": {},
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "これは酸っぱそうじゃのう！",
          "readings": {
            "酸っぱそう": "すっぱそう"
          },
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ウマ娘のヒシミラクルちゃんがレモンを食べてる絵だね！",
          "readings": {
            "ヒシミラクル": "ヒシミラクル"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "顔がすっぱそうだよ！",
          "readings": {
            "すっぱそう": "すっぱそう"
          },
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "Image",
        "data": {
          "action": "show",
          "format": "web",
          "image_url": "https://lohas.nicoseiga.jp/thumb/11431820i"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "レモンは酸っぱいからのう",
          "readings": {},
          "facialExpression": "ふくれっ面"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "わしも昔食べて顔がしかめっ面になったことがあるわい",
          "readings": {
            "しかめっ面": "しかめっつら"
          },
          "facialExpression": "ふくれっ面"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "こみーもレモン食べたことあるんだ！",
          "readings": {},
          "facialExpression": "ウィンク"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "アタシも食べてみたーい！",
          "readings": {},
          "gesture": "お嬢様笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "しゃろんにはまだ早いと思うぞ",
          "readings": {},
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "それにしても、はるとろさんが描いたヒシミラクルの表情がとてもリアルじゃな",
          "readings": {
            "はるとろ": "はるとろ",
            "リアル": "リアル"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "そうだね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "すっぱくて目が回っちゃってる感じが伝わってくるよ！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "はるとろさんの絵、すごいね！",
          "readings": {
            "はるとろ": "はるとろ"
          },
          "gesture": "喜んだ時のブイサイン"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ウマ娘ファンの間でも話題になっとるようじゃな",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "流行りのレモンを使った面白い発想じゃ",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ヒシミラクルちゃんの新しい一面が見れた気がするよ！はるとろさんの絵の",
          "readings": {
            "はるとろ": "はるとろ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "力だね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "title",
          "text": null
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "caption",
          "text": null
        }
      },
      {
        "command": "Pause",
        "data": {
          "duration": 2
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "title",
          "text": "im11431609【悔い多き世界線の鳳翔さん】"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "caption",
          "text": "投稿者：ツンイチ"
        }
      },
      {
        "command": "Image",
        "data": {
          "action": "show",
          "format": "web",
          "image_url": "https://lohas.nicoseiga.jp/thumb/11431609i"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "おおお！",
          "readings": {},
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "これは艦これの鳳翔さんがνガンダムになっとるのう！",
          "readings": {
            "νガンダム": "ニューガンダム",
            "艦これ": "かんこれ"
          },
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "艦娘とガンダムのコラボじゃな",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "わぁ、かっこいい！",
          "readings": {},
          "gesture": "喜んだ時のブイサイン"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "鳳翔さんがロボットになってるよ！",
          "readings": {},
          "gesture": "喜んだ時のブイサイン"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "フィン・ファンネルがいっぱい飛んでるね！",
          "readings": {
            "フィン・ファンネル": "フィンファンネル"
          },
          "gesture": "挑発ポーズ"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ファンネルは遠隔操作の武器じゃな",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "νガンダムの代名詞的な装備じゃ",
          "readings": {
            "νガンダム": "ニューガンダム"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "鳳翔さんもファンネルで敵をやっつけるんじゃろうのう",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ふふふ、鳳翔さんがロボットになって戦うのって面白いね！",
          "readings": {},
          "gesture": "お嬢様笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ツンイチさんのアイデアが素晴らしいよ！",
          "readings": {
            "ツンイチ": "つんいち"
          },
          "gesture": "指を指して肯定する"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ほんまじゃのう",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "艦これとガンダムという人気作品のコラボで、ファンにはたまらん作品じゃろうて",
          "readings": {
            "艦これ": "かんこれ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "わしも艦これはよう知らんが、このイラストは迫力があっていいのう",
          "readings": {
            "艦これ": "かんこれ"
          },
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "そうだね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "二つの世界が合わさって、新しい物語が生まれてるみたい！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "ツンイチさんの創造力に拍手！",
          "readings": {},
          "gesture": "喜んだ時のブイサイン"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "うむ",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ほんならこのイラストの紹介はこれぐらいにしとくかのう",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "みんなも気になったら、ニコニコ静画でツンイチさんの作品をチェックしてみてくだされ〜",
          "readings": {
            "ニコニコ静画": "ニコニコせいが"
          },
          "facialExpression": "ウィンク"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "title",
          "text": null
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "caption",
          "text": null
        }
      },
      {
        "command": "Corner",
        "data": {
          "action": "end",
          "name": "静画紹介"
        }
      }
    ]
  },
  {
    "name": "daily_events",
    "commands": [
      {
        "command": "Corner",
        "data": {
          "action": "start",
          "name": "本日の出来事紹介"
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
          "charaId": 3,
          "text": "みなさん、こんにちは！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "今日は2024年5月14日ですね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そういえば、今日は1888年に明治唱歌第1集が発行された日なんだよね",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "title",
          "text": "1888年5月14日 - 明治唱歌第1集発行"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "へぇ、明治唱歌って何だろう…？",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "クーちゃん、詳しく教えてくれる？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
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
          "charaId": 4,
          "text": "明治唱歌は明治時代の小学校の音楽教育のための唱歌集なんだ",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "1872年の学制で小学校の教科に唱歌が定められたんだけど、",
          "readings": {
            "学制": "ガクセイ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "当初はあまり普及しなかったんだよね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "でも、1888年頃から民間出版の唱歌集が出始めて、",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "明治唱歌第1集もその一つなんだ",
          "readings": {},
          "facialExpression": "ドヤ顔"
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
          "charaId": 3,
          "text": "なるほどね…",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "明治唱歌ってどんな曲が入ってるの？",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "明治唱歌第1集には「窓をあける」とか「赤とんぼ」、「うみ」など、",
          "readings": {
            "赤とんぼ": "アカトンボ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "今でも親しまれてる曲が収録されてるんだ",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "あぁ、「赤とんぼ」は知ってるよ！",
          "readings": {
            "赤とんぼ": "アカトンボ"
          },
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "優しくて懐かしい感じの歌だよね",
          "readings": {},
          "facialExpression": "目を見開く"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そうそう",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "明治唱歌は国民の道徳心や愛国心を育てるのが目的だったんだ",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "明治時代の音楽教育や国民教化の一環として、重要な役割を果たしたんだよ",
          "readings": {
            "国民教化": "コクミンキョウカ"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "title",
          "text": null
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
          "charaId": 3,
          "text": "クーちゃんは明治唱歌についてよく知ってるんだね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "まぁね…",
          "readings": {},
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "でも明治唱歌は日本の音楽教育の歴史の中で重要なんだよ",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "その後も唱歌教育は発展していって、1907年には小学校の必須科目になったんだ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "へぇ…",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "そういう歴史があったんだね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "勉強になったよ！",
          "readings": {},
          "facialExpression": "通常"
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
          "charaId": 4,
          "text": "うん、今日は明治唱歌第1集発行の記念日だったね",
          "readings": {
            "明治唱歌": "メイジショウカ"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "みんなも童謡とかに親しんでみるといいかも！",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "そうだね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 3,
          "text": "童謡って心が和むし、日本の文化も感じられるから面白いよね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "Pause",
        "data": {
          "duration": 2
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "あたりちゃん、今日5月14日に起こったことで他に何か面白いのあった？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そういえば、5月14日って特撮ドラマの主人公の誕生日なんだよね",
          "readings": {
            "特撮": "トクサツ"
          },
          "facialExpression": "目を見開く",
          "facing": "character:2"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "へぇ〜、どんな特撮ドラマなの？",
          "readings": {
            "特撮": "トクサツ"
          },
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "caption",
          "text": "ポリス×戦士 ラブパトリーナ!"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "「ポリス×戦士 ラブパトリーナ!」っていうんだ",
          "readings": {
            "ポリス×戦士 ラブパトリーナ!": "ポリスクロスセンシ ラブパトリーナ"
          },
          "facialExpression": "ドヤ顔",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "2020年から2021年にかけてテレビ東京系列で放送されてた少女向けの",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "特撮ドラマだよ",
          "readings": {
            "特撮": "トクサツ"
          },
          "facialExpression": "ドヤ顔",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "主人公の子の誕生日が今日なんだね",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "主人公ってどんな子なの？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "Camera",
        "data": {
          "camId": 2
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "caption",
          "text": "主人公：愛羽ツバサ"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "主人公は愛羽ツバサっていう女の子なんだけど、ツバサの母親が小説家の",
          "readings": {
            "愛羽ツバサ": "アイバツバサ"
          },
          "facialExpression": "ドヤ顔",
          "facing": "camera:2"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "愛羽優って人で、「名探偵マグレ」シリーズを書いてるんだって",
          "readings": {
            "愛羽優": "アイバユウ",
            "名探偵マグレ": "メイタンテイマグレ"
          },
          "facialExpression": "ドヤ顔",
          "facing": "camera:2"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "ふ〜ん…でも、ツバサちゃんの生年月日はプロフィールに書いてなかったんだよね〜",
          "readings": {},
          "facialExpression": "目をそらす",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "ちょっと残念だなぁ…",
          "readings": {},
          "facialExpression": "目をそらす",
          "facing": "character:4"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "caption",
          "text": null
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
          "charaId": 4,
          "text": "ま、生年不明ってことは、ツバサは何歳でも演じられるってことだからいいんじゃない？",
          "readings": {},
          "facialExpression": "苦笑い",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "これからもラブでパパッとタイホしてほしいね！",
          "readings": {
            "タイホ": "逮捕"
          },
          "facialExpression": "苦笑い",
          "gesture": "頑張れ！",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "そうだね！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "ツバサちゃん、お誕生日おめでとう！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "これからも頑張ってね！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "Pause",
        "data": {
          "duration": 2
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そして次の5月14日のできごとは...",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "title",
          "text": "5月14日のできごと"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "うんうん、次は何かな...？",
          "readings": {},
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "小説『化物語』で阿良々木暦（あららぎ こよみ）と八九寺真宵（はちくじ まよい）が",
          "readings": {
            "阿良々木暦": "あららぎ こよみ",
            "八九寺真宵": "はちくじ まよい",
            "『化物語』": "ばけものがたり"
          },
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "出会ったんだって",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "show",
          "position": "caption",
          "text": "小説『化物語』より"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "ファンタジー小説の中の出来事なんだね...！",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "でも、5月14日って何か関係あるのかな...？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "実は小説の中ではいつ出会ったのか正確な日付は書かれてないんだよね...",
          "readings": {},
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "でも、5月って新学期が始まる季節だから、クラスメイトとして出会うには",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ぴったりの時期なんだよ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "なるほど...！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "新学期に新しい出会いがあるのは、現実世界でも小説の中でも同じなんだね",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そうそう",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "小説の中では、主人公の暦くんが春休み中に吸血鬼に襲われて怪我をしたんだけど",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "...",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "その怪我が異常に早く治ったことがきっかけで、いろんな不思議な出来事に",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "巻き込まれていくんだ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "え、吸血鬼!? こわいよ...",
          "readings": {},
          "facialExpression": "目を見開く",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "でも、怪我が早く治るのは良いことなのかな...？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そこから暦くんは、体重を奪われて5kgしかないクラスメイトの女の子、",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ひたぎを助けることになるんだ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "体重が5kg!? そんなの絶対おかしいよね...",
          "readings": {},
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "ひたぎさん、大丈夫なのかな...",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ひたぎを助けるために、暦くんは委員長の翼や、怪異に詳しいメメさんたちの",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "力を借りるんだ",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "みんなで力を合わせて、ひたぎの問題を解決していくお話なんだよ",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "みんなで協力し合うのは大事だよね",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "怪異のこと、よくわかんないけど...きっと友達の力があれば何とかなるよね！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "そうだね",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ひたぎは最初は暦くんに毒舌だったみたいだけど、助けてもらったことで",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "段々と打ち解けていくみたい",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "新学期の出会いが、こんな大きな冒険のきっかけになるなんて面白いよね！",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "新学期の出会いって、一生の友達になるかもしれないからワクワクするよね",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "私たちも、これからどんな冒険が待ってるのかな...！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "うん、私たちも新学期を迎えたばかりだし、これから楽しいことがいっぱい",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "ありそうだよね！",
          "readings": {},
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "今日は小説の中の出来事を見てきたけど、現実の新学期の出会いも大切に",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "していきたいな",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "そうだね、あたりちゃん！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "新しいクラスのみんなとも仲良くなれたらいいな...",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "これからの学校生活、がんばろうね！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:4"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "うん、一緒にがんばろう、クーちゃん！",
          "readings": {},
          "facialExpression": "ドヤ顔"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "というわけで、今日は5月14日にまつわる小説の出来事を見てきました！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "caption",
          "text": null
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "新学期のドキドキわくわくな雰囲気を感じられたかな...？",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 2,
          "text": "現実世界の新学期も、素敵な出会いがあるといいですね！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "今日のできごと紹介コーナーは以上です！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 4,
          "text": "それじゃあまたね！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "Telop",
        "data": {
          "action": "hide",
          "position": "title",
          "text": null
        }
      },
      {
        "command": "Corner",
        "data": {
          "action": "end",
          "name": "本日の出来事紹介"
        }
      }
    ]
  },
  {
    "name": "ending",
    "commands": [
      {
        "command": "Corner",
        "data": {
          "action": "start",
          "name": "エンディング"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "今日のニコニコ倶楽部はいかがでしたか？",
          "readings": {}
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "娯楽あたりのゲーセンエピソードはびっくりしましたねー！",
          "readings": {
            "娯楽": "ごらく",
            "娯楽あたり": "ごらくあたり"
          },
          "facialExpression": "通常"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "でも、隣の人には申し訳なかったそうなので、ちゃんと謝ったんでしょうかッ？",
          "readings": {},
          "facialExpression": "苦笑い"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "あの子は良い子じゃけど、ちょっと行動力がありすぎるのう",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "でも、あれで良い体験談ができたんじゃからよかったんじゃないかのー",
          "readings": {},
          "facialExpression": "目をそらす",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "そうですねー",
          "readings": {},
          "facing": "character:1"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "ちょっとした失敗も、楽しい思い出になるものですッ！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "character:1"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "それから、今日紹介された静画もすごかったですねー",
          "readings": {
            "静画": "せいが"
          },
          "facialExpression": "通常",
          "facing": "character:1"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "ほんまじゃのー",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "あのνガンダムになった鳳翔（ほうしょう）さんかっこよかったのう",
          "readings": {
            "νガンダム": "ニューガンダム",
            "鳳翔": "ほうしょう"
          },
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "二つの世界が混ざり合って、新しいストーリーが生まれとるんが面白いのー",
          "readings": {},
          "facialExpression": "ウィンク",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "5月は新しい出会いの季節ですからねー",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "小説の中でも、暦（こよみ）くんとひたぎさんが出会って、冒険が始まるみたいですッ！",
          "readings": {
            "暦": "こよみ"
          },
          "facialExpression": "目を見開く",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "これからどんな物語が展開するのか、わたしもわくわくしちゃいますッ！",
          "readings": {},
          "facialExpression": "ドヤ顔",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "わしも楽しみじゃのー",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "それじゃあ、今日のニコニコ倶楽部はここまでじゃな",
          "readings": {},
          "facialExpression": "通常",
          "facing": "character:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "みんなも良い出会いがありますようにのー",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 1,
          "text": "それじゃあ、また来週ーッ！",
          "readings": {},
          "gesture": "頑張れ！",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "今日も見てくださってありがとうございましたッ！",
          "readings": {},
          "facialExpression": "通常",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "来週もお楽しみにーッ！",
          "readings": {},
          "facialExpression": "ウィンク",
          "facing": "camera:0"
        }
      },
      {
        "command": "TalkScript",
        "data": {
          "charaId": 0,
          "text": "ニコニコ倶楽部、おしまいっ！",
          "readings": {},
          "gesture": "喜んだ時のブイサイン",
          "facing": "camera:0"
        }
      },
      {
        "command": "Corner",
        "data": {
          "action": "end",
          "name": "エンディング"
        }
      }
    ]
  }
]
```

# 感想

（バグ修正が多くて出力は上記の一回しかまだできていない）

確かに気持ち的にキャラクターたちの性格がもっと出ていて、 ChatGPT の出力が対照的に硬い？と感じる。

ただし冒頭で関係図の内容をそのまま言ってしまっているのは気になる（「クーちゃん、素直でいいですね！」はほぼ関係図そのまま）。

現在はテキストの途中に表情・ジェスチャー変化のコマンドを出力させていて、Python 側で変化の時点で区切っているけど、表情・ジェスチャーがもっと使ってくれている反面変なところで区切ってしまうことがあるので Python 側も調整必要かも（あるいは形式を変える？）。

## セリフ形式提案

**現在**

```json
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "text": "いろんな表情とジェスチャーがあるセリフ",
    "readings": {},
    "facialExpression": "ウィンク",
    "gesture": "喜んだ時のブイサイン",
    "facing": "camera:0"
  }
}
```

**提案**

```json
{
  "command": "TalkScript",
  "data": {
    "charaId": 0,
    "segments": [
      {
        "text": "いろんな"
      },
      {
        "text": "表情",
        "facialExpression": "ウィンク"
      },
      {
        "text": "と"
      },
      {
        "text": "ジェスチャー",
        "gesture": "喜んだ時のブイサイン"
      },
      {
        "text": "があるセリフ"
      }
    ],
    "readings": {},
    "facing": "camera:0"
  }
}
```
