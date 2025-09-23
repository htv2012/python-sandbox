from types import SimpleNamespace

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


@pytest.mark.parametrize(
    "obj, path, default, expected",
    [
        pytest.param(None, "foo", None, None, id="obj is None, expect None"),
        pytest.param(None, "foo", "bar", "bar", id="obj is None, expect default"),
        pytest.param(test_obj, ".name", None, "Object Name", id="attribute"),
        pytest.param(test_obj, "name", None, "Object Name", id="attribute, no dot"),
        pytest.param(test_obj, "tags[1]", None, "tag1", id="list element"),
        pytest.param(test_obj, "phone[home]", None, "555-1212", id="dictionary"),
        pytest.param(test_obj, "commands[0].name", None, "command1", id="combo"),
        pytest.param(
            test_obj, "commands[0].result.output", None, "Hello", id="nested1"
        ),
        pytest.param(
            test_obj, "commands[0].result.foo", None, None, id="error in leaf"
        ),
        pytest.param(
            test_obj, "tags[:3]", None, ["tag0", "tag1", "tag2"], id="slice, first N"
        ),
        pytest.param(
            test_obj, "tags[3:]", None, ["tag3", "tag4"], id="slice, from N on"
        ),
        pytest.param(test_obj, "tags[4:2:-1]", None, ["tag4", "tag3"], id="reversed"),
        pytest.param(test_obj, "tags[1:2:3:4]", None, None, id="invalid slice"),
    ],
)
def test_kai(obj, path, default, expected):
    if default is None:
        actual = kai(obj, path)
    else:
        actual = kai(obj, path, default)
    assert actual == expected
