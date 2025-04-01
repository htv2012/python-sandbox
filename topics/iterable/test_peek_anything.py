import peek_anything
import pytest


@pytest.mark.parametrize(
    ["iterable", "default", "first", "rest"],
    [
        pytest.param(iter([1, 2, 3]), None, 1, [1, 2, 3], id="iterable"),
        pytest.param(iter([]), "foo", "foo", [], id="empty iterable"),
        pytest.param([1, 2, 3], None, 1, [1, 2, 3], id="list"),
        pytest.param([], "foo", "foo", [], id="empty list"),
        pytest.param((1, 2, 3), None, 1, [1, 2, 3], id="tuple"),
    ],
)
def test_peek(iterable, default, first, rest):
    actual_first, actual_rest = peek_anything.peek(iterable, default)
    assert actual_first == first
    assert list(actual_rest) == rest
