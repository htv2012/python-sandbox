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
    assert "Deleted: ['a']" in tracked.changes


def test_addition(tracked):
    tracked["c"] = "foo"
    assert "Updated: ['c']='foo'" in tracked.changes


def test_update(tracked):
    tracked["a"] = "bar"
    assert "Updated: ['a']='bar'" in tracked.changes


def test_update_many(tracked):
    tracked.update({"a": "bar", "c": "foo"})
    assert "Updated: ['c']='foo'" in tracked.changes
    assert "Updated: ['a']='bar'" in tracked.changes


def test_add_then_delete(tracked, original):
    tracked["new"] = "foo"
    del tracked["new"]
    assert dict(tracked) == original


def test_add_then_delete_existing_key(tracked):
    tracked["a"] = "foo"
    del tracked["a"]
    assert dict(tracked) == dict(b=2)
