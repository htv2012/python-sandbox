#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "bs4>=0.0.2",
#     "requests>=2.34.2",
# ]
# ///
import argparse
import io
import json
import os
import pathlib
import re
import urllib.parse
from typing import Optional

import bs4
import requests

QUERY = """query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    boundTopicId
    title
    titleSlug
    content
    translatedTitle
    translatedContent
    isPaidOnly
    difficulty
    likes
    dislikes
    isLiked
    similarQuestions
    contributors {
      username
      profileUrl
      avatarUrl
      __typename
    }
    langToValidPlayground
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    companyTagStats
    codeSnippets {
      lang
      langSlug
      code
      __typename
    }
    stats
    hints
    solution {
      id
      canSeeDetail
      __typename
    }
    status
    sampleTestCase
    metaData
    judgerAvailable
    judgeType
    mysqlSchemas
    enableRunCode
    enableTestMode
    envInfo
    libraryUrl
    __typename
  }
}
"""


PYPROJECT = """[tool.pytest.ini_options]
log_cli="true"
log_level="DEBUG"
markers=["slow"]
"""

MAKE = """quick: lint
	PYTHONPATH=.. pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=.. pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=.. pytest -s -vv . ../common

lint: format
	ruff check . ../common --fix

format:
	ruff format . ../common
	ruff check --select I --fix . ../common

cp:
	grep --color=never -E -v '^from (common|nary_tree|tree|list_node)' solution.py | xsel -b
"""


CONFTEST_TEMPLATE = """import pytest

from solution import Solution


@pytest.fixture
def fut():
    # Function under test
    sol = Solution()
    return sol.%s
"""

ENV = "PYTHONPATH=..\n"

SETTINGS = """{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
"""

SOLUTION_TEMPLATE = """from typing import List, Optional
from common import nary_tree, tree, list_node

%s
"""


def extract_slug(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.path.split("/")[2]


def parse_var(text: str):
    key, value = text.split(" = ")
    value = json.loads(value)
    return key, value


def parse_test_case(example: bs4.element.Tag):
    test_id = example.text.removesuffix(":")
    var_list = {}
    pre = example.find_next("pre")
    for line in pre.text.splitlines():
        if "Input: " in line:
            var_list.update(
                parse_var(token) for token in line.removeprefix("Input: ").split(", ")
            )
        elif line.startswith("Output: "):
            var_list["expected"] = json.loads(line.removeprefix("Output: "))
    return test_id, var_list


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

    details["dir"] = f"{question['questionFrontendId']}. {question['title']}"

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

    return details


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--root",
        type=pathlib.Path,
        default=pathlib.Path("~/Projects/interview-questions/leetcode").expanduser(),
    )
    parser.add_argument("-d", "--dump")
    parser.add_argument("url")
    options = parser.parse_args()

    details = extract_details(options.url, options.dump)

    # Determine the root: leetcode dir
    assert options.root.exists()
    os.chdir(options.root)

    # Create directories and files
    project_dir = options.root / details["dir"]
    project_dir.mkdir()
    vscode_dir = project_dir / ".vscode"
    vscode_dir.mkdir()

    (project_dir / ".env").write_text(ENV)
    (project_dir / "conftest.py").write_text(CONFTEST_TEMPLATE % details["fut"])
    (project_dir / "Makefile").write_text(MAKE)
    (project_dir / "pyproject.toml").write_text(PYPROJECT)
    (project_dir / "solution.py").write_text(SOLUTION_TEMPLATE % details["code"])
    (project_dir / "test_solution.py").write_text(details["test"])
    (vscode_dir / "settings.json").write_text(SETTINGS)

    pathlib.Path("/tmp/leetdir").write_text(f"cd {project_dir}")


if __name__ == "__main__":
    main()
