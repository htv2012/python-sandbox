import pytest


def test_simple_assume():
    """This method reports all failure."""
    x, y = 5, 10
    pytest.assume(x == y)
    pytest.assume(x > 10)


def test_using_context_manager():
    """This method reports only the last failure. Could be a bug."""
    with pytest.assume:
        assert 3 > 10
        assert 3 % 2 == 0
