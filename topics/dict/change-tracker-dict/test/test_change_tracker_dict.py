import pytest

from change_tracker_dict import ChangeTrackerDict


@pytest.fixture
def original():
    return dict(a=1, b=2)


@pytest.fixture
def tracked(original):
    return ChangeTrackerDict(original)


def test_no_change(tracked):
    assert not tracked.changed


def test_deletion(tracked):
    del tracked["a"]
    assert [("delete", "a", None)] == tracked.changes


def test_pop_existing_key_with_default(tracked):
    assert tracked.pop("a", "default") == 1
    assert [("delete", "a", None)] == tracked.changes


def test_pop_existing_key_without_default(tracked):
    tracked.pop("a")
    assert [("delete", "a", None)] == tracked.changes


def test_pop_with_default(tracked):
    assert tracked.pop("foo", "bar") == "bar"
    assert [("delete", "foo", None)] == tracked.changes


def test_pop_without_default(tracked):
    with pytest.raises(KeyError, match="foo"):
        tracked.pop("foo")


def test_addition(tracked):
    tracked["c"] = "foo"
    assert [("update", "c", "foo")] == tracked.changes


def test_update(tracked):
    tracked["a"] = "bar"
    assert [("update", "a", "bar")] == tracked.changes


def test_update_many(tracked):
    tracked.update({"a": "bar", "c": "foo"})
    assert [("update", "a", "bar"), ("update", "c", "foo")] == tracked.changes


def test_add_then_delete(tracked, original):
    tracked["new"] = "foo"
    del tracked["new"]
    assert dict(tracked) == original


def test_add_then_delete_existing_key(tracked):
    tracked["a"] = "foo"
    del tracked["a"]
    assert dict(tracked) == dict(b=2)
