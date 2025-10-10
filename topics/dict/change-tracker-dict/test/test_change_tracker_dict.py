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
