from types import SimpleNamespace

import pytest

from kai_drill import kai

from .common import tc

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


@pytest.mark.parametrize(
    "tc",
    [
        tc(
            "obj is None, expect None",
            obj=None,
            path="foo",
            default=None,
            expected=None,
        ),
        tc(
            "obj is None, expect default",
            obj=None,
            path="foo",
            default="bar",
            expected="bar",
        ),
        tc(
            "attribute",
            obj=test_obj,
            path=".name",
            default=None,
            expected="Object Name",
        ),
        tc(
            "attribute without dot",
            obj=test_obj,
            path="name",
            default=None,
            expected="Object Name",
        ),
        tc(
            "list element",
            obj=test_obj,
            path="tags[1]",
            default=None,
            expected="tag1",
        ),
        tc(
            "dictionary",
            obj=test_obj,
            path="phone[home]",
            default=None,
            expected="555-1212",
        ),
        tc(
            "combo",
            obj=test_obj,
            path="commands[0].name",
            default=None,
            expected="command1",
        ),
        tc(
            "nested1",
            obj=test_obj,
            path="commands[0].result.output",
            default=None,
            expected="Hello",
        ),
        tc(
            "error in leaf",
            obj=test_obj,
            path="commands[0].result.foo",
            default=None,
            expected=None,
        ),
        tc(
            "slice, first N",
            obj=test_obj,
            path="tags[:3]",
            default=None,
            expected=["tag0", "tag1", "tag2"],
        ),
        tc(
            "slice, from N on",
            obj=test_obj,
            path="tags[3:]",
            default=None,
            expected=["tag3", "tag4"],
        ),
        tc(
            "slice, reversed",
            obj=test_obj,
            path="tags[4:2:-1]",
            default=None,
            expected=["tag4", "tag3"],
        ),
        tc(
            "slice, invalid",
            obj=test_obj,
            path="tags[1:2:3:4]",
            default=None,
            expected=None,
        ),
    ],
)
def test_kai(tc):
    if tc.default is None:
        actual = kai(tc.obj, tc.path)
    else:
        actual = kai(tc.obj, tc.path, tc.default)
    assert actual == tc.expected
