import collections

import pytest

from leet.parse import parse_output

from .testlib import t


@pytest.mark.parametrize(
    "test_data",
    [
        t("single bool", intext="Output: true\n", ok=True, expected={"expected": True}),
        t("single int", intext="Output: 91", ok=True, expected={"expected": 91}),
        t(
            "single list",
            intext="Output: [1,3,12,0,0]\n",
            ok=True,
            expected={"expected": [1, 3, 12, 0, 0]},
        ),
        t(
            "list of str",
            intext='Output: ["o","l","l","e","h"]\n',
            ok=True,
            expected={"expected": ["o", "l", "l", "e", "h"]},
        ),
        t("not output line", intext="foo", ok=False, expected={}),
    ],
)
def test_parse_output(test_data):
    lines = collections.deque([test_data.intext])
    ok, value = parse_output(lines)

    assert ok is test_data.ok
    assert value == test_data.expected
