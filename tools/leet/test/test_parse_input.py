import collections

import pytest

from leet.parse import parse_multi_line_input, parse_single_line_input

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
    lines = collections.deque([test_data.intext])
    assert parse_single_line_input(lines) == (test_data.ok, test_data.parsed)


@pytest.mark.parametrize(
    "test_case",
    [
        t(
            "two lists",
            intext='Input\n["MyStack", "push", "push", "top", "pop", "empty"]\n[[], [1], [2], [], [], []]\nOutput\n',
            ok=True,
            parsed={
                "in1": ["MyStack", "push", "push", "top", "pop", "empty"],
                "in2": [[], [1], [2], [], [], []],
            },
        ),
        t(
            "input without colon",
            intext='Input\n["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]\nOutput',
            ok=True,
            parsed={
                "in1": [
                    "MagicDictionary",
                    "buildDict",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                "in2": [
                    [],
                    [["hello", "leetcode"]],
                    ["hello"],
                    ["hhllo"],
                    ["hell"],
                    ["leetcoded"],
                ],
            },
        ),
        t(
            "input with colon",
            intext='Input:\n["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]\n[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]\n\nOutput:',
            ok=True,
            parsed={
                "in1": [
                    "Router",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "forwardPacket",
                    "addPacket",
                    "getCount",
                ],
                "in2": [
                    [3],
                    [1, 4, 90],
                    [2, 5, 90],
                    [1, 4, 90],
                    [3, 5, 95],
                    [4, 5, 105],
                    [],
                    [5, 2, 110],
                    [5, 100, 110],
                ],
            },
        ),
        t("non-input line", intext="foo", ok=False, parsed={}),
    ],
)
def test_parse_multi_line_input(test_case):
    lines = collections.deque(test_case.intext.splitlines())
    ok, parsed = parse_multi_line_input(lines)
    assert ok is test_case.ok
    assert parsed == test_case.parsed
