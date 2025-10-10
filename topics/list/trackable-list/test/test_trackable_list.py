import pytest

from trackable_list import TrackableList


@pytest.fixture
def lut():
    """List under test"""
    return TrackableList(["Peter", "Paul", "Mary"])


def test_access(lut):
    lut[0]
    assert lut.transactions == [("get", 0, "Peter", None)]
    lut[2]
    assert lut.transactions == [("get", 0, "Peter", None), ("get", 2, "Mary", None)]


def test_set(lut):
    lut[0] = "John"
    assert lut.transactions == [("set", 0, "John", "Peter")]


def test_append(lut):
    lut.append("John")
    assert lut.transactions == [("insert", 3, "John", None)]


def test_delete(lut):
    del lut[0]
    assert lut.transactions == [("delete", 0, None, "Peter")]


def test_insert(lut):
    lut.insert(0, "John")
    assert list(lut) == ["John", "Peter", "Paul", "Mary"]


def test_replace_slice(lut):
    lut[:1] = ["John", "George"]
    assert lut.transactions == [
        ("set", slice(None, 1, None), ["John", "George"], ["Peter"])
    ]
