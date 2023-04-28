[« langchain 使ってみた](./02_langchain.md)

# 概要

ツールをもっと工夫すれば LLM にとって使いやすくなるのかな？

# ニコニコ動画検索ツール

```
Searches for videos on ニコニコ動画
Action Input must be a JSON object in the following format:
{
    "query": "日本語の検索キーワードの文字列、オプショナル",
    "genre": optional string, one of ['animal', 'anime', 'commentary_lecture', 'cooking', 'dance', 'entertainment', 'game', 'music_sound', 'nature', 'other', 'r18', 'radio', 'society_politics_news', 'sports', 'traveling_outdoor', 'technology_craft', 'vehicle'],
    "uploaded before": optional string, ISO-format datetime (JST),
    "uploaded after": optional string, ISO-format datetime (JST),
    "include description": optional boolean, default false, whether to include video description in search results,
    "sort by": string, one of ['uploadTime', 'viewCount', 'mylistCount', 'likeCount', 'commentCount'],
    "sort order": string, one of ['ascending', 'descending'],
    "page": optional int, page of search results, default 0
}
"sort by" and "sort order" are mandatory
"page" starts at 0, increase it for more search results
```

# データを直接 LLM に渡さないという発想

langchain に Python を実行するツールがある

検索結果をそのまま LLM に渡すとトークン数が大変なことになるし重い

ならば、**データを渡さずに、　 Python で扱ってもらうのはどう？**

# 実験

**入力**: "Current time: {datetime.datetime.now()}\nOut of anime, game, and music_sound, which genre had the most overall likes last year? Follow a step-by-step plan, gathering one piece of information at a time, and execute only one action at a time until you reach the final answer"

**過程**

```
> Entering new AgentExecutor chain...
I need to search for videos in each genre and filter by upload date to only include videos from last year. Then I need to sort the results by like count and find the genre with the highest total likes.
Action: NicoNico video search
Action Input:
{
    "genre": "anime",
    "uploaded before": "2022-01-01T00:00:00+09:00",
    "uploaded after": "2021-01-01T00:00:00+09:00",
    "sort by": "likeCount",
    "sort order": "descending",
    "page": 0
}
Observation: Seach results stored in variable `search_results_0` with format [{'genre': ..., 'playlistCount': ..., 'viewCount': ..., 'title': ..., 'commentCount': ..., 'likeCount': ...}, ...]. Variable can be accessed from Python interpreter
I need to repeat the previous action for the other two genres and store the results in separate variables.
Action: NicoNico video search
Action Input:
{
    "genre": "game",
    "uploaded before": "2022-01-01T00:00:00+09:00",
    "uploaded after": "2021-01-01T00:00:00+09:00",
    "sort by": "likeCount",
    "sort order": "descending",
    "page": 0
}
Observation: Seach results stored in variable `search_results_1` with format [{'genre': ..., 'playlistCount': ..., 'viewCount': ..., 'title': ..., 'commentCount': ..., 'likeCount': ...}, ...]. Variable can be accessed from Python interpreter
I need to repeat the previous action for the last genre and store the results in a separate variable.
Action: NicoNico video search
Action Input:
{
    "genre": "music_sound",
    "uploaded before": "2022-01-01T00:00:00+09:00",
    "uploaded after": "2021-01-01T00:00:00+09:00",
    "sort by": "likeCount",
    "sort order": "descending",
    "page": 0
}
Observation: Seach results stored in variable `search_results_2` with format [{'genre': ..., 'playlistCount': ..., 'viewCount': ..., 'title': ..., 'commentCount': ..., 'likeCount': ...}, ...]. Variable can be accessed from Python interpreter
I need to sum up the total likes for each genre and compare them to find the genre with the highest total likes.
Action: Python interpreter
Action Input:
total_likes_anime = sum([result['likeCount'] for result in search_results_0])
total_likes_game = sum([result['likeCount'] for result in search_results_1])
total_likes_music = sum([result['likeCount'] for result in search_results_2])
if total_likes_anime > total_likes_game and total_likes_anime > total_likes_music:
    print('Anime had the most overall likes last year')
elif total_likes_game > total_likes_anime and total_likes_game > total_likes_music:
    print('Game had the most overall likes last year')
else:
    print('Music_sound had the most overall likes last year')
Observation: Game had the most overall likes last year
I have found the genre with the most overall likes last year.
Final Answer: Game had the most overall likes last year.

> Finished chain.
```
