import collections

import pytest

from leet.parse import parse_multi_line_output, parse_output

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


@pytest.mark.parametrize(
    "test_data",
    [
        t(
            "output without colon",
            intext="Output\n[null, null, null, 2, 2, false]\n\n",
            ok=True,
            parsed={"expected": [None, None, None, 2, 2, False]},
        ),
        t(
            "output with colon",
            intext="Output:\n[null, true, true, false, true, true, [2, 5, 90], true, 1]\n\n",
            ok=True,
            parsed={
                "expected": [None, True, True, False, True, True, [2, 5, 90], True, 1]
            },
        ),
    ],
)
def test_parse_multi_line_output(test_data):
    lines = collections.deque(test_data.intext.splitlines())
    ok, parsed = parse_multi_line_output(lines)

    assert ok is test_data.ok
    assert parsed == test_data.parsed
