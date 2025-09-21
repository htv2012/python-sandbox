from types import SimpleNamespace

import pytest

from kai_drill import kai

test_obj = SimpleNamespace(
    name="Object Name",
    tags=["tag0", "tag1"],
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
        pytest.param(
            test_obj, "commands[0].result.output", None, "Hello", id="nested1"
        ),
        pytest.param(
            test_obj, "commands[0].result.foo", None, None, id="error in leaf"
        ),
    ],
)
def test_kai(obj, path, default, expected):
    if default is None:
        actual = kai(obj, path)
    else:
        actual = kai(obj, path, default)
    assert actual == expected
