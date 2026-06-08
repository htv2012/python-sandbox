import pytest

from leet.parse import parse_output

from .testlib import t


@pytest.mark.parametrize(
    "test_data",
    [
        t("single bool", intext="Output: true\n", expected=True),
        t("single int", intext="Output: 91", expected=91),
        t(
            "single list",
            intext="Output: [1,3,12,0,0]\n",
            expected=[1, 3, 12, 0, 0],
        ),
        t(
            "list of str",
            intext='Output: ["o","l","l","e","h"]\n',
            expected=["o", "l", "l", "e", "h"],
        ),
    ],
)
def test_parse_output(test_data):
    assert parse_output(test_data.intext) == test_data.expected
