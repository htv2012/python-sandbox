import pytest

from solution import Solution


@pytest.fixture
def rev():
    return Solution().reverse


@pytest.mark.parametrize(
    "input_int,expected",
    [
        pytest.param(123, 321, id="example 1"),
        pytest.param(-123, -321, id="example 2"),
        pytest.param(120, 21, id="example 3"),
    ],
)
def test_reverse_int(input_int, expected, rev):
    assert rev(input_int) == expected
