import pytest

from scb.data import STACK_CAPCACITY, Stack


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
    stack = _create_stack(range(STACK_CAPCACITY))
    assert stack.is_full
    assert not stack.is_empty


def test_push_pop():
    stack = _create_stack(range(STACK_CAPCACITY))

    out = []
    while not stack.is_empty:
        out.append(stack.pop())

    assert stack.is_empty
    assert out == [7, 6, 5, 4, 3, 2, 1, 0]


def test_is_completed():
    stack = _create_stack("a" * STACK_CAPCACITY)
    assert stack.is_completed


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([], [" "] * 8, id="empty"),
        pytest.param(["a"], [" "] * 7 + ["a"], id="not full"),
        pytest.param("abcdefg", [" "] + list("gfedcba"), id="almost full"),
        pytest.param(range(STACK_CAPCACITY), [7, 6, 5, 4, 3, 2, 1, 0], id="full"),
    ],
)
def test_iter(values, expected):
    stack = _create_stack(values)
    assert list(stack) == expected
