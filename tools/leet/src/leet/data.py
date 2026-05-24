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
