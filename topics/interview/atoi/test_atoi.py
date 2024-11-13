import pytest

from solution import LOWER_BOUND, UPPER_BOUND, Solution


@pytest.fixture
def atoi():
    solution = Solution()
    return solution.myAtoi


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param("42", 42, id="ex1"),
        pytest.param("   -42", -42, id="ex2"),
        pytest.param("4193 with words", 4193, id="ex3"),
        pytest.param("", 0, id="empty_str"),
        pytest.param("hello", 0, id="no_digit_found"),
        pytest.param("   - ", 0, id="negative_sign_only"),
        pytest.param(str(LOWER_BOUND), LOWER_BOUND, id="at_lower"),
        pytest.param(str(UPPER_BOUND), UPPER_BOUND, id="at_upper"),
        pytest.param(str(LOWER_BOUND - 1), LOWER_BOUND, id="below_lower"),
        pytest.param(str(UPPER_BOUND + 1), UPPER_BOUND, id="above_upper"),
    ],
)
def test_atoi(input_str, expected, atoi):
    actual = atoi(input_str)
    assert actual == expected
