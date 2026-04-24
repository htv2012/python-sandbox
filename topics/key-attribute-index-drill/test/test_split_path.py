import dataclasses
from typing import Any, Optional

import pytest
from common import context

from kai_drill import TokenKind, split_path


@dataclasses.dataclass
class SplitPathTestCase:
    __test__ = False
    path: Any
    expected: Optional[Any] = None
    exception: Optional[Exception] = None

    @classmethod
    def make(
        cls,
        id: str,
        path: str,
        expected: Optional[Any] = None,
        exception: Optional[Exception] = None,
    ):
        return pytest.param(cls(path, expected, exception), id=id)


@pytest.mark.parametrize(
    "test_case",
    [
        #
        # Happy-path cases
        #
        SplitPathTestCase.make(
            id="index", path="[0]", expected=[(0, TokenKind.KEY_OR_INDEX)]
        ),
        SplitPathTestCase.make(
            id="slice1",
            path="[:3]",
            expected=[(slice(None, 3), TokenKind.KEY_OR_INDEX)],
        ),
        SplitPathTestCase.make(
            id="key", path="[_key_1]", expected=[("_key_1", TokenKind.KEY_OR_INDEX)]
        ),
        SplitPathTestCase.make(
            id="key with spaces",
            path="[tally total]",
            expected=[("tally total", TokenKind.KEY_OR_INDEX)],
        ),
        SplitPathTestCase.make(
            id="key with dashes",
            path="[tally-total]",
            expected=[("tally-total", TokenKind.KEY_OR_INDEX)],
        ),
        SplitPathTestCase.make(
            id="attribute", path=".attr", expected=[("attr", TokenKind.ATTRIBUTE)]
        ),
        SplitPathTestCase.make(
            id="combo",
            path="[_key_2].attr[0]",
            expected=[
                ("_key_2", TokenKind.KEY_OR_INDEX),
                ("attr", TokenKind.ATTRIBUTE),
                (0, TokenKind.KEY_OR_INDEX),
            ],
        ),
        #
        # Error cases
        #
        SplitPathTestCase.make(
            id="missing dot or left bracket", path="foo", exception=ValueError
        ),
        SplitPathTestCase.make(id="wrong type, int", path=1, exception=TypeError),
        SplitPathTestCase.make(id="wrong type, None", path=None, exception=TypeError),
        # Bad char: space
        SplitPathTestCase.make(
            id="spaces before attribute", path=" .foo", exception=ValueError
        ),
        SplitPathTestCase.make(
            id="spaces before bracket", path=" [foo]", exception=ValueError
        ),
        SplitPathTestCase.make(
            id="ends with spaces", path=".foo ", exception=ValueError
        ),
        # Bad char: other
        SplitPathTestCase.make(id="bad char: <", path="<.foo", exception=ValueError),
    ],
)
def test_path_split(test_case):
    with context(test_case.exception):
        assert split_path(test_case.path) == test_case.expected
