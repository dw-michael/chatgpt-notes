import datetime
import io
import json
import os
import re
import sys
import textwrap
from typing import Optional

import langchain.agents
import langchain.chat_models
import langchain.llms
import langchain.memory
import langchain.tools
import langchain.utilities
import pydantic
import requests

os.environ["OPENAI_API_KEY"] = "OPEN API KEY HERE"


def text_to_json(text: str):
    """Parse possibly unclean JSON, like from a language model output."""
    text = text.strip("`")
    if "{" in text:
        text = text[text.index("{") :]
    else:
        text = "{" + text
    if "}" in text:
        text = text[: text.rindex("}") + 1]
    else:
        text = text + "}"
    parsed = json.loads(text)
    # Remove nulls
    parsed = {k: v for k, v in parsed.items() if v is not None}
    return parsed


class PythonREPL(pydantic.BaseModel):
    """Modified version of langchain's PythonREPL.

    Due to quirks with how exec works, care must be taken with passing
    globals and locals. In general, globals should be None, and locals
    should contain the environment to pass.
    """

    globals: Optional[dict] = pydantic.Field(default_factory=dict, alias="_globals")
    locals: Optional[dict] = pydantic.Field(default_factory=dict, alias="_locals")

    def run(self, command: str) -> str:
        """Run command with own globals/locals and returns anything printed."""
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        try:
            exec(
                command,
                self.globals if self.globals else None,
                self.locals if self.locals else None,
            )
            output = mystdout.getvalue()
        except Exception as e:
            output = repr(e)
        finally:
            sys.stdout = old_stdout
        return output


class NicoSearchTool(langchain.tools.BaseTool):
    class Config:
        extra = pydantic.Extra.allow

    name = "NicoNico video search"

    sort_keys = ["uploadTime", "viewCount", "mylistCount", "likeCount", "commentCount"]
    sort_orders = ["ascending", "descending"]

    genre_lookup = {
        "animal": "動物",
        "anime": "アニメ",
        "commentary_lecture": "解説・講座",
        "cooking": "料理",
        "dance": "ダンス",
        "entertainment": "エンターテイメント",
        "game": "ゲーム",
        "music_sound": "音楽・サウンド",
        "nature": "自然",
        "other": "その他",
        "r18": "R-18",
        "radio": "ラジオ",
        "society_politics_news": "社会・政治・時事",
        "sports": "スポーツ",
        "traveling_outdoor": "旅行・アウトドア",
        "technology_craft": "技術・工作",
        "vehicle": "乗り物",
    }
    response_format = textwrap.dedent(
        f"""\
        {{{{
            "query": "日本語の検索キーワードの文字列、オプショナル",
            "genre": optional string, one of {list(genre_lookup)},
            "uploaded before": optional string, ISO-format datetime (JST),
            "uploaded after": optional string, ISO-format datetime (JST),
            "include description": optional boolean, default false, whether to include video description in search results,
            "sort by": string, one of {sort_keys},
            "sort order": string, one of {sort_orders},
            "page": optional int, page of search results, default 0
        }}}}"""
    )

    targets = "title,description,tags"
    fields = (
        "title,genre,description,viewCounter,mylistCounter,likeCounter,commentCounter"
    )

    field_aliases = {
        "durationInSeconds": "lengthSeconds",
        "viewCount": "viewCounter",
        "likeCount": "likeCounter",
        "favoriteCount": "mylistCounter",
        "commentCount": "commentCounter",
        "uploaderId": "userId",
        "uploadTime": "startTime",
    }
    field_aliases_rev = {v: k for k, v in field_aliases.items()}

    description = textwrap.dedent(
        f"""\
        Searches for videos on ニコニコ動画
        Action Input must be a JSON object in the following format:
        {textwrap.indent(response_format, '        ').strip()}
        "sort by" and "sort order" are mandatory
        "page" starts at 0, increase it for more search results
        Results contain title, genre, description (if requested), as well as
        view, favorite, like, and comment counts"""
    )

    def __init__(
        self,
        llm,
        description_limit: int = 50,
        results_per_page: int = 10,
    ):
        super().__init__()
        self._llm = llm
        self._description_limit = description_limit
        self._rpp = results_per_page

    def _validate_parsed_query(self, parsed: dict):
        """Ensure all required keys are present and in proper format."""
        for key in ["sort by", "sort order"]:
            assert key in parsed, f'Missing mandatory key "{key}"'
            assert isinstance(parsed[key], str), f'Value of "{key}" must be string'
        assert (
            parsed["sort by"] in self.sort_keys
        ), f'Value of "sort by" must be one of {self.sort_keys}'
        assert (
            parsed["sort order"] in self.sort_orders
        ), f'Value of "sort order" must be one of {self.sort_orders}'
        for key in ["uploaded before", "uploaded after"]:
            if key in parsed:
                try:
                    datetime.datetime.fromisoformat(parsed[key])
                except ValueError as e:
                    raise AssertionError(
                        f'Invalid ISO format for "{key}" with value: {parsed[key]}'
                    )
        if "query" in parsed:
            assert isinstance(parsed["query"], str), 'Value of "query" must be string'
        if "genre" in parsed:
            assert (
                parsed["genre"] in self.genre_lookup
            ), f'Value of "genre" must be one of {list(self.genre_lookup)}'
        if "include description" in parsed:
            assert isinstance(
                parsed["include description"], bool
            ), 'Value of "include description" must be bool'
        if "page" in parsed:
            assert isinstance(parsed["page"], int), 'Value of "page" must be int'
            assert parsed["page"] >= 0, '"page" must be 0 or higher'

    def _try_parse_query(self, query: str, max_attempts: int = 3) -> dict:
        """Attempt to parse and validate query, using LLM to fix if needed."""
        for attempt in range(max_attempts):
            try:
                parsed = text_to_json(query)
                self._validate_parsed_query(parsed)
                return parsed
            except (json.JSONDecodeError, AssertionError) as e:
                if attempt + 1 == max_attempts:
                    raise RuntimeError(
                        f"Max attempts ({max_attempts}) exceeded for query {query}"
                    )
                prompt = "Given the following incorrect input JSON, error message, and schema, respond with a corrected JSON object.\n"
                prompt += f"Input:\n{query}\nError message: {e}\nSchema:\n{self.response_format}"
                query = self._llm(prompt)

    def _format_datetime(self, dt: str) -> str:
        return (
            datetime.datetime.fromisoformat(dt)
            .replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
            .isoformat(timespec="seconds")
        )

    def _make_request_params(self, params: dict) -> dict:
        """Convert LLM-style parameters to API-style parameters."""
        sort_prefix = "-" if params["sort order"] == "descending" else ""
        sort = self._alias_to_field(params["sort by"])
        offset = self._rpp * params.get("page", 0)
        converted = {
            "q": params.get("query", ""),
            "targets": self.targets,
            "fields": self.fields,
            "_sort": sort_prefix + sort,
            "_offset": offset,
            "_limit": self._rpp,
            "_context": "gpt-agent-test",
        }
        if maxdate := params.get("uploaded before"):
            converted["filters[startTime][lt]"] = self._format_datetime(maxdate)
        if mindate := params.get("uploaded after"):
            converted["filters[startTime][gt]"] = self._format_datetime(mindate)
        if not params.get("include description", False):
            converted["fields"] = converted["fields"].replace(",description", "")
        if genre := params.get("genre"):
            converted["filters[genre][0]"] = self.genre_lookup[genre]
        return converted

    def _alias_to_field(self, alias: str) -> str:
        """Convert LLM-style aliases to API-style fields."""
        return self.field_aliases.get(alias, alias)

    def _replace_field_with_alias(self, text: str) -> str:
        """Replace API-style fields with LLM-style aliases in text."""
        for original, alias in self.field_aliases_rev.items():
            text = text.replace(original, alias)
        return text

    def _clean_response(self, resp) -> str:
        """Convert an API response to a clean string output.

        Uses an LLM to summarize long video descriptions if needed.
        """
        if resp.status_code == 200:
            data = resp.json()["data"]
            if not data:
                return "No search results found\n"
            for item in data:
                if desc := item.get("description"):
                    desc = re.sub(r"<[^>]+>", "", desc)
                    if len(desc) > self._description_limit:
                        prompt = f"Below is the description of a video. Summarize it in Japanese in at most {self._description_limit} characters. "
                        prompt += "Focus on describing the content of the video, and remove any "
                        prompt += "HTML, formatting, line breaks, references to social media, calls to action, etc.\n"
                        prompt += f"Description:\n{desc}"
                        desc = self._llm(prompt).replace("\n", "")
                    item["description"] = desc
            return self._replace_field_with_alias(
                re.sub(
                    r"\\u([0-9a-f]{4})",
                    lambda match: chr(int(match.group(1), 16)),
                    json.dumps(data),
                )
            )
        return self._replace_field_with_alias("Error from search API: " + resp.text)

    def _fetch(self, params: dict):
        """Call search API using given API parameters."""
        request_params = self._make_request_params(params)
        resp = requests.get(
            "https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search",
            params=request_params,
            headers={
                "User-Agent": "gpt-agent-test",
            },
        )
        return self._clean_response(resp) + "\n"

    def _run(self, query: str) -> str:
        """Attempt to run the given query."""
        try:
            params = self._try_parse_query(query)
        except Exception as e:
            return f"Failed to parse Action Input, try again (Error: {e})\n"
        return self._fetch(params)

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Test API does not run asynchronously")


class NicoPythonTool:
    """Combined tool that maintains saved variables for the Python environment."""

    def __init__(
        self,
        llm,
        description_limit: int = 60,
        results_per_page: int = 10,
    ):
        self._llm = llm
        self._nico = NicoSearchTool(llm, description_limit, results_per_page)
        self._python = langchain.utilities.PythonREPL()
        self._variables = {}

    def _save_variable(self, var_name: str, data):
        """Custom function for Python interpreter tool."""
        self._variables[var_name] = data
        print(f"# Saved variable `{var_name}`")

    def _load_variable(self, var_name):
        """Custom function for Python interpreter tool.

        Not explicitly stated to be a provided function,
        but the LLM sometimes attempts to call this,
        so provide it anyway
        """
        if data := self._variables.get(var_name):
            return data
        raise KeyError(f"Variable {var_name} does not exist")

    def _python_run_nico(self, params: dict) -> str:
        """Nico search function for Python interpreter tool."""
        self._nico._validate_parsed_query(params)
        res = self._nico._fetch(params)
        if not res.startswith("Error"):
            return json.loads(res)
        return res

    def _python_run_llm(self, instructions: str, data_desc: str, data):
        """LLM function for Python interpreter tool."""
        prompt = "Complete the following task using the following data.\n"
        prompt += f"Task: {instructions}\n"
        prompt += f"Description of data: {data_desc}\n"
        prompt += f"Data:\n{data}"
        return self._llm(prompt)

    def _run_python(self, code: str) -> str:
        """Python interpreter tool function."""
        # llm sometimes wraps code in Markdown-style backticks. Remove them
        code = code.strip().strip("`")
        # Create environment
        env = {
            "save_variable": self._save_variable,
            "load_variable": self._load_variable,
            "search_nico": self._python_run_nico,
            "llm": self._python_run_llm,
        }
        env.update(self._variables)
        response = PythonREPL(_locals=env).run(code)
        return response

    def _run_nico(self, query: str) -> str:
        """Nico search tool function."""
        search_result = self._nico(query)
        if not search_result.startswith("["):
            return search_result
        result = json.loads(search_result)
        varname = f"search_results_{len(self._variables)}"
        self._variables[varname] = result
        result_schema = str({k: None for k in result[0]}).replace("None", "...")
        result_schema = f"[{result_schema}, ...]"
        response = f"Found {len(result)} search results, stored in variable `{varname}` with format {result_schema}. "
        response += "Variable can be accessed from Python interpreter"
        return response

    def _run_llm(self, query: str) -> str:
        """LLM tool function."""
        parsed = text_to_json(query)
        for key in ["instructions", "data variable", "data description"]:
            if key not in parsed:
                return f'Action Input must contain key "{key}"'
        instructions = parsed["instructions"]
        var_name = parsed["data variable"]
        data_desc = parsed["data description"]
        if var_name not in self._variables:
            return (
                f"Error: variable {var_name} does not exist. "
                f"Available variables: {list(self._variables)}"
            )
        data = self._variables[var_name]
        return self._python_run_llm(instructions, data_desc, data)

    @property
    def python_tool(self):
        return langchain.agents.Tool(
            name="Python interpreter",
            func=self._run_python,
            description="Executes Python code. "
            "Useful for performing calculations or other programmatic logic. "
            "Previous search results will be available as variables. "
            "You also have access to the special function `save_variable(variable_name: str, data: Any)` "
            "which can be called to save data as variables. "
            "These variables can automatically be accessed by name in future calls to the Python interpreter. "
            "The final output must be passed to a print() function.",
        )

    @property
    def nico_tool(self):
        return langchain.agents.Tool(
            name=self._nico.name,
            func=self._run_nico,
            description=self._nico.description,
        )

    @property
    def llm_tool(self):
        return langchain.agents.Tool(
            name="Language model",
            func=self._run_llm,
            description="Uses a language model to perform NLP tasks on data.\n"
            "Has a token limit, so pass only necessary data, and be explicit and detailed with instructions.\n"
            "Action Input must be a JSON object in the following format:\n"
            "{{\n"
            '    "instructions": "Task for language model, such as summarizing text or extracting information",\n'
            '    "data description": "Explanation of what the data represents",'
            '    "data variable": "Name of variable containing data to analyze. Only one variable at a time"\n'
            "}}\n"
            "Can also be called from Python interpreter as `llm(instructions: str, description: str, data: Any)`",
        )


class SafeOutputAgent:
    """Wrapper that catches OutputParserErrors that still contain correct answers."""

    def __init__(self, agent, llm):
        self.agent = agent
        self._llm = llm

    def _validate_final_answer(self, query: str, response: str) -> bool:
        """Use an LLM to determine if the invalid output was still a valid answer."""
        prompt = "Below are the task given to a system and the system's response. "
        prompt += "Determine if the system produced a valid response, or if something went wrong, like an error. "
        prompt += "A response is valid even if it is factually wrong or unhelpful, as long as it answers the question. "
        prompt += "Respond only YES or NO: YES if the response is valid, NO if the response is invalid.\n"
        prompt += f"Task: {query}\n"
        prompt += f"System response: {response}"
        evaluation = self._llm(prompt).lower().strip()
        return "yes" in evaluation and "no" not in evaluation

    def run(self, query: str) -> str:
        try:
            return self.agent.run(query)
        except langchain.agents.mrkl.output_parser.OutputParserException as e:
            error_text = str(e)
            if "Could not parse LLM output: `" in error_text:
                text = error_text.replace("Could not parse LLM output: `", "").strip(
                    "`"
                )
                if self._validate_final_answer(query, text):
                    return text
            raise e


def main():
    llm = langchain.chat_models.ChatOpenAI(temperature=0.2)
    nico_python_tool = NicoPythonTool(langchain.llms.OpenAI(), 100, 15)
    tools = [
        nico_python_tool.nico_tool,
        nico_python_tool.python_tool,
        nico_python_tool.llm_tool,
    ]
    agent = SafeOutputAgent(
        langchain.agents.initialize_agent(
            tools,
            llm,
            agent=langchain.agents.AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        ),
        langchain.llms.OpenAI(),
    )

    agent.run("Write prompt here")


if __name__ == "__main__":
    main()
