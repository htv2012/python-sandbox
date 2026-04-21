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
    def param(cls, desc: str, **kwargs):
        return pytest.param(cls(**kwargs), id=desc)


@pytest.mark.parametrize(
    "tc",
    [
        KaiTestCase.param(
            "obj is None, expect None",
            obj=None,
            path=".foo",
            default=None,
            expected=None,
        ),
        KaiTestCase.param(
            "obj is None, expect default",
            obj=None,
            path=".foo",
            default="bar",
            expected="bar",
        ),
        KaiTestCase.param(
            "attribute",
            obj=test_obj,
            path=".name",
            default=None,
            expected="Object Name",
        ),
        KaiTestCase.param(
            "list element",
            obj=test_obj,
            path=".tags[1]",
            default=None,
            expected="tag1",
        ),
        KaiTestCase.param(
            "dictionary",
            obj=test_obj,
            path=".phone[home]",
            default=None,
            expected="555-1212",
        ),
        KaiTestCase.param(
            "combo",
            obj=test_obj,
            path=".commands[0].name",
            default=None,
            expected="command1",
        ),
        KaiTestCase.param(
            "nested1",
            obj=test_obj,
            path=".commands[0].result.output",
            default=None,
            expected="Hello",
        ),
        KaiTestCase.param(
            "error in leaf",
            obj=test_obj,
            path="commands[0].result.foo",
            default=None,
            expected=None,
        ),
        KaiTestCase.param(
            "slice, first N",
            obj=test_obj,
            path=".tags[:3]",
            default=None,
            expected=["tag0", "tag1", "tag2"],
        ),
        KaiTestCase.param(
            "slice, from N on",
            obj=test_obj,
            path=".tags[3:]",
            default=None,
            expected=["tag3", "tag4"],
        ),
        KaiTestCase.param(
            "slice, reversed",
            obj=test_obj,
            path=".tags[4:2:-1]",
            default=None,
            expected=["tag4", "tag3"],
        ),
        KaiTestCase.param(
            "slice, invalid",
            obj=test_obj,
            path="tags[1:2:3:4]",
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
