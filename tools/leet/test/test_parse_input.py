import pytest

from leet.parse import parse_single_line_input

from .testlib import t


@pytest.mark.parametrize(
    "test_data",
    [
        t("single bool", intext="Input: t = true", ok=True, parsed={"t": True}),
        t("single int", intext="Input: n = 19\n", ok=True, parsed={"n": 19}),
        t(
            "multiple vars",
            intext="Input: head = [1,2,6,3,4,5,6], val = 6\n",
            ok=True,
            parsed={"head": [1, 2, 6, 3, 4, 5, 6], "val": 6},
        ),
        t(
            "multiple vars, string",
            intext='Input: s = "egg", t = "add"\n',
            ok=True,
            parsed={"s": "egg", "t": "add"},
        ),
        t("invalid, input without colon", intext="Input", ok=False, parsed={}),
    ],
)
def test_parse_single_line_input(test_data):
    assert parse_single_line_input(test_data.intext) == (test_data.ok, test_data.parsed)
