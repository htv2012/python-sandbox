import collections
import io
import json
import re
import urllib
import urllib.parse
from typing import Optional

import bs4
import html2text
import requests

from .data import QUERY


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


def parse_single_line_input(text: str):
    if not text.startswith("Input: "):
        return False, {}

    text = text.removeprefix("Input: ").strip()
    tokens = text.split(", ")

    name_value = {}
    for token in tokens:
        name, value = token.split(" = ")
        value = json.loads(value)
        name_value[name] = value

    return True, name_value


# def parse_input(text: str):
#     parsers = [parse_single_line_input]
#     for parser in parsers:
#         ok, parsed = parser(text)
#         if ok:
#             return ok, parsed
#     return False, f"Cannot parse: {text!r}"


def parse_test_id(lines: collections.deque):
    line = lines.popleft()
    if line.startswith("Example "):
        test_id = line.strip().removesuffix(":")
        return True, {"test_id": test_id}
    lines.appendleft(line)
    return False, None


def parse_test_case(content: str):
    lines = collections.deque(content.splitlines())
    data_list = []
    parsers = [parse_test_id, parse_single_line_input, parse_output]
    test_data = {}

    while lines:
        for parser in parsers:
            ok, parsed = parser(lines)
            if not ok:
                continue

            test_data.update(parsed)
            if "expected" in parsed:
                data_list.append((test_data))
                test_data = {}
            break

    return data_list


def extract_details(url: str, dump: Optional[str]) -> dict:
    details = {}

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

    soup = bs4.BeautifulSoup(question["content"], "html.parser")
    examples = dict(
        parse_test_case(node) for node in soup.find_all("strong", class_="example")
    )

    var_names = []
    for test_case in examples.values():
        var_names = list(test_case)
        break

    buffer = io.StringIO()
    buffer.write('"""\n')
    buffer.write(f"{url}\n")
    buffer.write('"""\n\n')
    buffer.write("import pytest\n\n\n")
    buffer.write("@pytest.mark.parametrize(\n")
    buffer.write(f"    {var_names},")
    buffer.write("    [\n")
    for test_id, example in examples.items():
        text = ", ".join(repr(v) for v in example.values())
        buffer.write(f"        pytest.param({text}, id={test_id!r}),\n")
    buffer.write("    ],\n")
    buffer.write(")\n")
    buffer.write("def test_solution(fut, ")
    buffer.write(", ".join(var_names))
    buffer.write("):\n")
    buffer.write(
        f"    assert fut({', '.join(v for v in var_names if v != 'expected')}) == expected"
    )
    details["test"] = buffer.getvalue()
    breakpoint()

    return details
