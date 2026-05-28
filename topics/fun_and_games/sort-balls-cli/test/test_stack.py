import pytest

from scb.stack import CAPACITY, EMPTY_VALUE, Stack


def _create_stack(values: list):
    stack = Stack()
    for value in values:
        stack.push(value)
    return stack


def test_empty():
    stack = Stack()
    assert stack.is_empty
    assert not stack.is_full


def test_full():
    stack = _create_stack(range(CAPACITY))
    assert stack.is_full
    assert not stack.is_empty


def test_push_pop():
    stack = _create_stack(range(CAPACITY))

    out = []
    while not stack.is_empty:
        out.append(stack.pop())

    assert stack.is_empty
    assert out == [7, 6, 5, 4, 3, 2, 1, 0]


def test_is_completed():
    stack = _create_stack("a" * CAPACITY)
    assert stack.is_completed


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([], [EMPTY_VALUE] * 8, id="empty"),
        pytest.param(["a"], [EMPTY_VALUE] * 7 + ["a"], id="not full"),
        pytest.param("abcdefg", [EMPTY_VALUE] + list("gfedcba"), id="almost full"),
        pytest.param(range(CAPACITY), [7, 6, 5, 4, 3, 2, 1, 0], id="full"),
    ],
)
def test_as_column(values, expected):
    stack = _create_stack(values)
    assert stack.as_column == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([], None, id="empty"),
        pytest.param("abc", "c", id="partial fill"),
        pytest.param(range(CAPACITY - 1), CAPACITY - 2, id="almost full"),
        pytest.param(range(CAPACITY), CAPACITY - 1, id="full"),
    ],
)
def test_top(values, expected):
    stack = _create_stack(values)
    assert stack.top == expected
