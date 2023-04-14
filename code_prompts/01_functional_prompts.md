# 概要

人のコードを読んでたら、「なるほど、コードを投げることもできるし、 JSON などの扱いやすい形式で返事してもらうこともできるんだね」と気づいた

もしかしてこうすると、もっとプログラム的な入力もできるし、もっと綺麗な返事がもらえるのでは？

日本語でも少しやってみたけど、やはり英語の方が自分的に書きやすいので一旦英語で遊んでみた。

# 関数 → JSON 会話ログ 1

**ユーザー**

> "You are an AI that understands commands written like Python function calls and responds only in strict JSON."

```python
# This function takes a list of topics and returns a joke about those topics.
# The return value is a JSON object with the keys "setup", "punchline"
def write_joke(topics: list[str]): ...

write_joke(["animals", "technology"])
```

**AI**

```json
{
  "setup": "Why did the cat join Facebook?",
  "punchline": "To keep in touch with its mice!"
}
```

**ユーザー**

```python
# This function takes a list of jokes and rates how funny they are from 1 to 5
# The return value is a JSON object with the keys:
# "jokes": an array of JSON objects representing the original jokes
# "ratings": an array of numbers representing the ratings
def rate_jokes(jokes: list[Joke]): ...

rate_jokes([
    write_joke(["music", "clown"]),
    write_joke(["computer", "apple pie"]),
    write_joke(["mathematician", "priest"]),
])
```

**AI**

```json
{
  "jokes": [
    {
      "setup": "Why did the pianist break a hand?",
      "punchline": "Because he only knew one octave!"
    },
    {
      "setup": "What did the computer say to the pie?",
      "punchline": "You're sweet but you've got a bad byte!"
    },
    {
      "setup": "Why did the mathematician become a priest?",
      "punchline": "He found a higher power!"
    }
  ],
  "ratings": [3, 4, 2]
}
```

これはかなり感心した。以前定義した関数をちゃんと使い回しできている。ただ AI のセンスを疑う。明らかに三番目が一番面白い。

この後、 JSON に不要なカンマを省いてくださいと指示して、以降の返事にちゃんと不要なカンマがなくなって Python の `json.loads()` で扱えるようになった。アプリで使うなら最初に不要なカンマについて注意すべきだね。あるいは Python としてパースしてもいいけど流石にちょっと危ない。

**ユーザー**

```python
# This function sorts the given shopping list by importance, with the most essential items first and the most optional items last.
# The return value is a JSON array that contains the shopping items in sorted order
def sort_shopping_list(items: list[str]): ...

sort_shopping_list(["eggs", "toilet paper", "cookies", "toys", "condoms", "tampons", "milk"])
```

**AI**

```json
["toilet paper", "eggs", "milk", "tampons", "cookies", "toys", "condoms"]
```

女性の方はどう思うのかわからないけど、まあ全体的に妥当かな？

**ユーザー**

```python
write_horror_story(topics=['werewolf', 'twin'], num_paragraphs=3)
```

実際アプリでこういう使い方をするなら、絶対返り値をちゃんと定義すると思うけど、興味本位で今回はコメントなしで試してみた。

関数呼び出しを読むだけでもやりたいことが大体わかるはず。

**AI**

```json
{
  "story": "In the darkness of the forest, a pair of twins stumbled upon a hidden cave. Little did they know that the cave was inhabited by a terrifying werewolf. Suddenly, they heard a faint growling that seemed to come from within the cave. The twins froze in terror as the growling grew louder and more ferocious.\n\nAs they tried to flee, they realized the werewolf was blocking their path. The creature was enormous, its eyes a chilling yellow, and its fur matted with blood. With a guttural roar, the werewolf lunged at the twins, and the air was filled with screams of horror and pain.\n\nThe rest of the villagers never found out what happened to the twins that night. All they could find were a few inseparable bones inside the cave, and the eerie silence that seemed to grip the forest forever."
}
```

ちゃんと 3 段落の「人狼」「双子」についてのホラーストーリーが返ってきた。あんまり面白いストーリーではないけどまあまあ。

**ユーザー**

```python
EMPLOYEE_ID | NAME          | SALARY
------------+---------------+------------
 152        | John Doe      | $50,000
 666        | Lucifer Satan | $66,666
 8675309    | Jenny Tutone  | $8,675,309
 007        | James Bond    | $100,300

# Returns JSON object with keys "id", "name"
def get_employee(criteria: str): ...

get_employee("highest paid")
```

**AI**

```json
{
  "id": "8675309",
  "name": "Jenny Tutone"
}
```

データベース（的なもの）を提供すればちゃんとクエリしてくれるね。正直 JSON のスキーマさえ定義すれば、プロンプトを関数呼び出しじゃなくて自然言語でも良さそう（関数のメリットもあるけど）

さらに面白いのは、 id を文字列にしてくれたこと。データベースに数字として不正な "007" が入っていたからかな？全部ちゃんとした数字だったらどうなるのかな？

さらにいくつかのクエリを投げてみたら答えてくれた：

```
>>> get_employee("most evil")

{
    "id": "666",
    "name": "Lucifer Satan"
}

>>> get_employee("best spy")

{
    "id": "007",
    "name": "James Bond"
}
```

**ユーザー**

```python
 ID | PRODUCT       | QUANTITY
----+---------------+----------
 1  | Chocolate bar | 35
 3  | Teddy bear    | 3
 4  | Toy car       | 8
 6  | Hand soap     | 69

# Returns JSON list of objects with keys "id", "name", "quantity"
def get_inventory_items(criteria: str, **kwargs): ...

get_inventory_items("toys")
```

**AI**

```json
[
  {
    "id": "4",
    "name": "Toy car",
    "quantity": 8
  }
]
```

なるほど、 id だから文字列だね。在庫が数字として解釈されたからカラム名を考慮しているみたい。
