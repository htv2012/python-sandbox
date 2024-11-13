import pytest

import solution


@pytest.fixture
def is_pal():
    return solution.Solution().isPalindrome


@pytest.mark.parametrize(
    "input_int,expected",
    [
        pytest.param(121, True, id="example 1"),
        pytest.param(-121, False, id="example 2"),
        pytest.param(-10, False, id="example 3"),
    ],
)
def test_pal(is_pal, input_int, expected):
    assert is_pal(input_int) is expected
