import dataclasses
from typing import Any, Optional

import pytest

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
        desc: str,
        path: str,
        expected: Optional[Any] = None,
        exception: Optional[Exception] = None,
    ):
        return pytest.param(cls(path, expected, exception), id=desc)


@pytest.mark.parametrize(
    "test_case",
    [
        #
        # Happy-path cases
        #
        SplitPathTestCase.make(
            "index", path="[0]", expected=[(0, TokenKind.KEY_OR_INDEX)]
        ),
        SplitPathTestCase.make(
            "slice1", path="[:3]", expected=[(slice(None, 3), TokenKind.KEY_OR_INDEX)]
        ),
        SplitPathTestCase.make(
            "key", path="[_key_1]", expected=[("_key_1", TokenKind.KEY_OR_INDEX)]
        ),
        SplitPathTestCase.make(
            "key with spaces",
            path="[tally total]",
            expected=[("tally total", TokenKind.KEY_OR_INDEX)],
        ),
        SplitPathTestCase.make(
            "key with dashes",
            path="[tally-total]",
            expected=[("tally-total", TokenKind.KEY_OR_INDEX)],
        ),
        SplitPathTestCase.make(
            "attribute", path=".attr", expected=[("attr", TokenKind.ATTRIBUTE)]
        ),
        SplitPathTestCase.make(
            "combo",
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
            "missing dot or left bracket", path="foo", exception=ValueError
        ),
        SplitPathTestCase.make("wrong type, int", path=1, exception=TypeError),
        SplitPathTestCase.make("wrong type, None", path=None, exception=TypeError),
        # Bad char: space
        SplitPathTestCase.make(
            "spaces before attribute", path=" .foo", exception=ValueError
        ),
        SplitPathTestCase.make(
            "spaces before bracket", path=" [foo]", exception=ValueError
        ),
        SplitPathTestCase.make("ends with spaces", path=".foo ", exception=ValueError),
        # Bad char: other
        SplitPathTestCase.make("bad char: <", path="<.foo", exception=ValueError),
    ],
)
def test_path_split(test_case):
    if test_case.exception is None:
        assert split_path(test_case.path) == test_case.expected
    else:
        with pytest.raises(test_case.exception):
            split_path(test_case.path)
