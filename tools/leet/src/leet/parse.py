import collections
import io
import itertools
import json
import re
import urllib
import urllib.parse
from typing import Optional, TextIO, TypedDict

import html2text
import requests

from .data import QUERY


class Details(TypedDict, total=False):
    readme: str
    project_id: str
    dir: str
    code: str
    test: str


NOT_PARSED = {}


def extract_slug(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.path.split("/")[2]


def parse_var(text: str):
    key, value = text.split(" = ")
    value = json.loads(value)
    return key, value


def parse_output(lines: collections.deque):
    line = lines.popleft()
    if line.startswith("Output: "):
        line = line.removeprefix("Output: ")
        line = line.strip()
        line = line.replace("'", '"')
        output = json.loads(line)
        return True, {"expected": output}
    lines.appendleft(line)
    return False, {}


def parse_multi_line_output(lines: collections.deque) -> tuple[bool, dict]:
    text = lines.popleft()
    if not (text.strip() == "Output" or text.strip() == "Output:"):
        lines.appendleft(text)
        return False, NOT_PARSED

    text = lines.popleft()
    value = json.loads(text)
    return True, {"expected": value}


def parse_single_line_input(lines: collections.deque):
    text = lines.popleft()
    if not text.startswith("Input: "):
        lines.appendleft(text)
        return False, {}

    text = text.removeprefix("Input: ").strip()
    tokens = text.split(", ")

    name_value = {}
    for token in tokens:
        name, value = token.split(" = ")
        value = json.loads(value)
        name_value[name] = value

    return True, name_value


def parse_multi_line_input(lines: collections.deque) -> tuple[bool, dict]:
    text = lines.popleft()
    if not (text.strip() == "Input" or text.strip() == "Input:"):
        lines.appendleft(text)
        return False, NOT_PARSED

    counter = itertools.count(1)
    input_vars = {}
    while (text := lines.popleft()).strip() not in {"Output", "Output:", ""}:
        name = f"in{next(counter)}"
        value = json.loads(text)
        input_vars[name] = value

    lines.appendleft(text)
    return True, input_vars


def parse_test_id(lines: collections.deque):
    line = lines.popleft()
    if line.startswith("Example "):
        test_id = line.strip().removesuffix(":")
        return True, {"test_id": test_id}
    lines.appendleft(line)
    return False, None


def parse_test_cases(content: str):
    lines = collections.deque(content.splitlines())
    data_list = []
    parsers = [
        parse_test_id,
        parse_single_line_input,
        parse_multi_line_input,
        parse_multi_line_output,
        parse_output,
    ]
    test_data = {}

    while lines:
        for parser in parsers:
            ok, parsed = parser(lines)
            if ok:
                test_data.update(parsed)
                if "expected" in parsed:
                    data_list.append((test_data))
                    test_data = {}
                break
        else:
            # Not handled, discard this line
            lines.popleft()

    return data_list


def write_param(test_case: dict, buf: TextIO):
    buf.write("        pytest.param(\n")
    buf.write("            types.SimpleNamespace(\n")
    for k, v in test_case.items():
        if k == "test_id":
            continue
        buf.write(f"                {k}={v!r},\n")
    buf.write("            ),\n")
    buf.write(f"            id={test_case['test_id']!r},\n")
    buf.write("        ),\n")


def write_test(test_cases: list[dict], buf: TextIO):
    buf.write("\n\n@pytest.mark.parametrize(\n")
    buf.write('    "test_case",\n')
    buf.write("    [\n")
    for test_case in test_cases:
        write_param(test_case, buf)
    buf.write("    ]\n")
    buf.write(")\n")
    buf.write("def test_solution(fut, test_case):\n")
    buf.write("    pass\n")


def write_script(url: str, test_cases: list[dict], buf: TextIO):
    buf.write('"""\n')
    buf.write(f"{url}\n")
    buf.write('"""\n\n')
    buf.write("import types\n")
    buf.write("\nimport pytest\n")
    write_test(test_cases, buf)


def extract_details(url: str, dump: Optional[str]) -> Details:
    details = Details()

    # Download the leetcode data
    slug = extract_slug(url)
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": QUERY,
    }

    response = requests.post("https://leetcode.com/graphql", json=payload)
    response.raise_for_status()
    response_json = response.json()
    if dump:
        with open(dump, "w") as stream:
            json.dump(response_json, stream, indent=4)
    question = response_json["data"]["question"]

    title = question["title"].lower().replace(" ", "_")
    qid = str(question["questionFrontendId"]).zfill(4)
    details["dir"] = f"leetcode_{qid}_{title}"
    details["project_id"] = f"leetcode-{qid}"

    converter = html2text.HTML2Text()
    details["readme"] = (
        f"# {question['title']}\n\n{converter.handle(question['content'])}"
    )

    buffer = io.StringIO()
    for snippet in question["codeSnippets"]:
        if snippet["lang"] == "Python3":
            code = snippet["code"].strip()
            for line in code.splitlines():
                buffer.write(f"{line}\n")
                if line.startswith("    def "):
                    details["fut"] = (
                        matched[1]
                        if (matched := re.search(r"def (\w+)", line))
                        else "unknown"
                    )
                    buffer.write(
                        f"        raise NotImplementedError({details['fut']!r})\n"
                    )
            details["code"] = buffer.getvalue()
            break

    # parse test cases and create the content of the test script
    test_cases = parse_test_cases(question["content"])
    buf = io.StringIO()
    write_script(url, test_cases, buf)
    details["test"] = buf.getvalue()

    return details
