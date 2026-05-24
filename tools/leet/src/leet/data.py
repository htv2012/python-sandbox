import pathlib
from typing import Optional

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


SETTINGS = """{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
"""


def get_template(name: str):
    here = pathlib.Path(__file__).parent
    template = here / "artifacts" / name
    with open(template) as stream:
        content = stream.read()
    return content


def write_file(root: pathlib.Path, name: str, content: Optional[str] = None):
    target = root / name
    content = content or get_template(name)
    target.write_text(content)
