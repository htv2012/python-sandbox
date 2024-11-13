import pytest

from linked_list import from_iterable


def test_from_iterable_empty():
    assert from_iterable([]) is None


@pytest.mark.parametrize(
    "inlist,expected",
    [
        pytest.param([1], [1], id="single node"),
        pytest.param([1, 2, 3], [1, 2, 3], id="multiple nodes"),
    ],
)
def test_from_iterable(inlist, expected):
    li = from_iterable(inlist)
    node = li
    for element in expected:
        assert node.val == element
        node = node.next
    assert node is None
