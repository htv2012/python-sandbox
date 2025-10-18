import pytest

from trackable_list import TrackableList


@pytest.fixture
def lut():
    """List under test"""
    return TrackableList(["Peter", "Paul", "Mary"])


def test_access(lut):
    lut[0]
    assert lut.transactions == [
        dict(action="get", index=0, prev_value=None, value="Peter")
    ]
    lut[2]
    assert lut.transactions == [
        dict(action="get", index=0, prev_value=None, value="Peter"),
        dict(action="get", index=2, prev_value=None, value="Mary"),
    ]


def test_set(lut):
    lut[0] = "John"
    assert lut.transactions == [
        dict(action="set", index=0, prev_value="Peter", value="John")
    ]


def test_append(lut):
    lut.append("John")
    assert lut.transactions == [
        dict(action="insert", index=3, prev_value=None, value="John")
    ]


def test_delete(lut):
    del lut[0]
    assert lut.transactions == [
        dict(action="delete", index=0, prev_value="Peter", value=None)
    ]


def test_insert(lut):
    lut.insert(0, "John")
    assert list(lut) == ["John", "Peter", "Paul", "Mary"]


def test_replace_slice(lut):
    lut[:1] = ["John", "George"]
    # assert lut.transactions == [ ("set", slice(None, 1, None), ["John", "George"], ["Peter"]) ]
    assert lut.transactions == [
        dict(
            action="set",
            index=slice(None, 1, None),
            prev_value=["Peter"],
            value=["John", "George"],
        )
    ]
