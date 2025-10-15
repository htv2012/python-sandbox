import pytest

from change_tracker_dict import MISSING, ChangeTrackerDict


@pytest.fixture
def original():
    return dict(a=1, b=2)


@pytest.fixture
def tracked(request, original):
    return ChangeTrackerDict(original)


def test_no_change(tracked):
    assert not tracked.dirty


def test_deletion(tracked):
    del tracked["a"]
    assert [dict(action="del", key="a", prev_value=1)] == tracked.changes


def test_pop_existing_key_with_default(tracked):
    assert tracked.pop("a", "default") == 1
    assert [dict(action="del", key="a", prev_value=1)] == tracked.changes


def test_pop_existing_key_without_default(tracked):
    tracked.pop("a")
    assert [dict(action="del", key="a", prev_value=1)] == tracked.changes


def test_pop_non_existing_key_with_default(tracked):
    assert tracked.pop("foo", "bar") == "bar"
    assert [] == tracked.changes


def test_pop_without_default(tracked):
    with pytest.raises(KeyError, match="foo"):
        tracked.pop("foo")


def test_addition(tracked):
    tracked["c"] = "foo"
    assert [
        dict(action="set", key="c", prev_value=MISSING, value="foo")
    ] == tracked.changes


def test_update(tracked):
    tracked["a"] = "bar"
    assert [dict(action="set", key="a", prev_value=1, value="bar")]


def test_update_many(tracked):
    tracked.update({"a": "bar", "c": "foo"})
    assert [
        dict(action="set", key="a", prev_value=1, value="bar"),
        dict(action="set", key="c", prev_value=MISSING, value="foo"),
    ] == tracked.changes


def test_add_then_delete(tracked, original):
    tracked["new"] = "foo"
    del tracked["new"]
    assert dict(tracked) == original


def test_add_then_delete_existing_key(tracked):
    tracked["a"] = "foo"
    del tracked["a"]
    assert dict(tracked) == dict(b=2)
