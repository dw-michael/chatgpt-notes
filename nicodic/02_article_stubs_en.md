[« 日本語プロンプト実験](./01_article_stubs.md)

# 概要

前に同じ、ただ指示は英語で。

自分的に英語が書きやすい＋モデルにとって理解しやすい（多分？）

# プロンプト

- (system) You are an assistant that writes wiki articles about ニコニコ動画 video tags. Please respond only in Japanese.
- Below are the titles and descriptions of videos tagged with 「{tag}」. Please write an introductory sentence that explains, in the simplest terms, what the tag is. Respond in Japanese, and write only one sentence.
- {返事}
- If a user wanted to write an article about this tag, what information should they research? Answer as a bullet-point list in Japanese. Respond with only the list and no introductory sentence
- {返事}

指示を英語で書くとしても、日本語をある程度混ぜないといけないことがわかった。あと「日本語で答えてください」と念を押さないと途中で英語になることもある。

# 結果

## 「枡久とうか」

> 「枡久とうか」とは、UTAU 音源を使用した楽曲制作においてのタグです。
>
> - 枡久とうかの由来と歴史
> - 枡久とうか音源の特徴と特色
> - 枡久とうかを使用した楽曲の例
> - 枡久とうか作成方法とその事例
> - 枡久とうかが使用されるコミュニティやイベント

**分析**

ちょっと惜しい。音声ライブラリであることを言って欲しかった。

記事に書くべきことのリストアップは結構良さそう。

## 「節約料理」

> 「節約料理」とは、予算に制限のある方々が工夫を凝らして美味しい料理を作るために用いるタグです。
>
> - 節約料理とは何か、どのような人たちが用いているかを調べる。
> - このタグが付けられた動画の種類や性質について調べ、一般的な特徴を把握する。
> - 節約料理に関連する商品やサービスが存在するかどうかを調べる。
> - 節約料理に関するブログや SNS の情報を把握する。
> - 節約料理の歴史や背景について調べ、その意義を解説する。

**分析**

二番目のプロンプトは工夫の余地がありそう。紹介文は日本語プロンプトの時と質が特に変わってない様子。

## 「sniper_elite3」

> 「sniper_elite3」は、ゲーム「Sniper Elite III」をプレイしたプレイヤーが制作した動画のタグです。
>
> - 「Sniper Elite III」とは何か
> - 「sniper_elite3」というタグを付けた動画がどのようなものか
> - 動画で取り扱っているトピックスは何か
> - ゲーム映像や実況音声の使用はどのように扱われているのか

**分析**

変な言い回しを使いがち？英語から日本語に翻訳しているせいかも？

提案した「調べるべきこと」も当たり前すぎてかつ曖昧すぎて、やはり日本語の回答が欲しかったら日本語でプロンプトすべき？

## 「遊戯王ナイトメアトラバドール」

> 「遊戯王ナイトメアトラバドール」は、ニコニコ動画上で公開されている「遊戯王」の実況動画のタグの一つです。
>
> - ゲームの概要やプレイの仕方
> - 「遊戯王ナイトメアトラバドール」に関連する実況動画の人気動画や作者
> - 「遊戯王ナイトメアトラバドール」の人気シリーズやエピソード
> - コメントやマイリス数などの反応
> - タグを活用した検索方法や使い方

**分析**

やはり言い方が不自然な気がする。調べるべきことのリストは悪くないが、最後の二つがイマイチ。
