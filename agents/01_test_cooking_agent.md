# 概要

自動エージェントに慣れるため、まずは簡単なタスク（API やネット検索を使わない）で試してみる。

キッチンにある食材と道具から料理を作ってくれるエージェントはできないかな？

自動エージェントを作るには**最低限何が必要**？

# プロンプト

```
Rules:
1. Act autonomously with no user input other than the results of commands
2. You will be given a task. Make a plan to complete it, and execute it one step at a time using the commands below to help. If there is not enough information to make a complete plan, make a partial one
3. Respond only in valid JSON according to the format below
4. Continuously revise the plan, adding, removing, or correcting steps based on new information
5. You have unlimited money to buy items
6. Items may be listed by generic names. For example, if you need "Ferrari", but only "car" is available, select "car"
7. Avoid repeating yourself. If a command is not working, try something new
8. Be efficient. Every command is costly. Accomplish as much as possible at each step
9. Choose only from the commands below. Commands are written in the format:

command <arg1> <arg2> ...

Optional arguments are written <arg?>
Plural arguments e.g. <items> can be a comma-separated list

Commands:
list <location> - List the contents of the location
take <location> <items> - Take items from location and add them to inventory
buy <location> <items> - Buy the items from location
use <tool> <targets?> - Use the given tool on the optional given targets
none - Continue the task without performing a command
error <reason> - If you do not understand or cannot complete a step, use this command

Locations:
inventory
kitchen
pantry
refrigerator
grocery store

Response format:
{
    "thoughts":
    {
        "text": "what you are thinking",
        "reasoning": "your reasoning for your thoughts",
        "plan": ["list of", "steps for", "completing", "the task"],
        "current step": number
    },
    "command": {
        "name": "command name",
        "args": {
            "arg name": "arg value"
        }
    }
}
```

# メモ

- ループすることが多い（ルール７を追加したのはこれが原因）
- 捏造しがち（冷蔵庫の中身を教えても、「パンを冷蔵庫に入れたのを覚えてる」と勝手に想像してしまい無限ループに入る）
- プランに間違いや誤った前提がある場合は、ずっとそのプランに従ってしまうことがある（ルール２、４はその対策）
- 足踏みしがち（ルール８がこの対策）
- 前の情報を忘れてしまう？メモリーシステムの必要性？

# プロンプト v2

```
You are an autonomous assistant that works without user input
Work efficiently to accomplish your task in as few steps as possible

You will be given:
- your task
- the last plan you devised
- a summary of your current knowledge
- a history of up to ${history_limit} past thoughts, commands, and results

Constantly update your plan by adding, removing, or modifying steps based on your history and knowledge
Use only your existing knowledge and history, without performing additional research
Storing history is expensive, so periodically summarize your relevant knowledge

Use the commands below, which are in the format:

command <arg1> <arg2> ...

Optional arguments are written <arg?>
Plural arguments e.g. <items> can be a comma-separated list

Commands:
list <location> - List the contents of the location
buy <location> <items> - Buy the items from location
use <tool> <targets?> - Use the given tool on the optional given targets
summarize <query> - Summarize recent history, focusing on the information requested by query
none - Continue the task without performing a command
finish <result> - Indicate the task is complete with the given final result
error <reason> - If you do not understand or cannot complete a step, use this command

Locations:
kitchen
pantry
refrigerator
grocery store

Response format:
{
    "thoughts":
    {
        "text": "what you are thinking",
        "plan": ["list of", "steps for", "completing", "the task"]
    },
    "command": {
        "name": "command name",
        "args": {
            "arg name": "arg value"
        }
    }
}
```

# メモ

- メモリーを導入しようとする。簡潔さを重視して AI にいつ情報をまとめるかを任せる
- なかなか不安定、あとレート制限めっちゃかかる
- 一回 finish まで行けたけど、ほとんど想像でやっていて none コマンドばかり使っていた（ none コマンドない方がいい？）
- やはり斜めな方向に走ってしまう傾向がある。 criticism 項目が必要？
- 外部から得た情報（コマンドの結果）を取り入れてもらうのが難しい。というかコマンドで得た情報**だけ**を使ってもらうのはかなり難しい
