import dataclasses
from types import SimpleNamespace
from typing import Any

import pytest

from kai_drill import kai

test_obj = SimpleNamespace(
    name="Object Name",
    tags=["tag0", "tag1", "tag2", "tag3", "tag4"],
    phone={"home": "555-1212", "work": "333-1111"},
    commands=[
        SimpleNamespace(
            name="command1",
            result=SimpleNamespace(
                exit_code=0,
                output="Hello",
            ),
        )
    ],
)


@dataclasses.dataclass
class KaiTestCase:
    obj: Any
    path: str
    default: Any
    expected: Any

    @classmethod
    def make(cls, id: str, **kwargs):
        return pytest.param(cls(**kwargs), id=id)


@pytest.mark.parametrize(
    "tc",
    [
        KaiTestCase.make(
            id="obj is None, expect None",
            obj=None,
            path=".foo",
            default=None,
            expected=None,
        ),
        KaiTestCase.make(
            id="obj is None, expect default",
            obj=None,
            path=".foo",
            default="bar",
            expected="bar",
        ),
        KaiTestCase.make(
            id="attribute",
            obj=test_obj,
            path=".name",
            default=None,
            expected="Object Name",
        ),
        KaiTestCase.make(
            id="list element",
            obj=test_obj,
            path=".tags[1]",
            default=None,
            expected="tag1",
        ),
        KaiTestCase.make(
            id="dictionary",
            obj=test_obj,
            path=".phone[home]",
            default=None,
            expected="555-1212",
        ),
        KaiTestCase.make(
            id="combo",
            obj=test_obj,
            path=".commands[0].name",
            default=None,
            expected="command1",
        ),
        KaiTestCase.make(
            id="nested1",
            obj=test_obj,
            path=".commands[0].result.output",
            default=None,
            expected="Hello",
        ),
        KaiTestCase.make(
            id="error in leaf",
            obj=test_obj,
            path=".commands[0].result.foo",
            default=None,
            expected=None,
        ),
        KaiTestCase.make(
            id="slice, first N",
            obj=test_obj,
            path=".tags[:3]",
            default=None,
            expected=["tag0", "tag1", "tag2"],
        ),
        KaiTestCase.make(
            id="slice, from N on",
            obj=test_obj,
            path=".tags[3:]",
            default=None,
            expected=["tag3", "tag4"],
        ),
        KaiTestCase.make(
            id="slice, reversed",
            obj=test_obj,
            path=".tags[4:2:-1]",
            default=None,
            expected=["tag4", "tag3"],
        ),
        KaiTestCase.make(
            id="slice, invalid",
            obj=test_obj,
            path=".tags[1:2:3:4]",
            default=None,
            expected=None,
        ),
    ],
)
def test_kai(tc: KaiTestCase):
    if tc.default is None:
        actual = kai(tc.obj, tc.path)
    else:
        actual = kai(tc.obj, tc.path, tc.default)
    assert actual == tc.expected
