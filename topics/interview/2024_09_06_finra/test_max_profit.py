import pytest

from profit import calculate_max_profit


@pytest.mark.parametrize(
    ["prices", "expected"],
    [
        pytest.param([4, 5, 9, 1, 3, 9, 2, 6], 8, id="case1"),
        pytest.param([4, 5, 9, 5, 3, 9, 2, 6], 6, id="case2"),
    ],
)
def test_profit(prices, expected):
    assert calculate_max_profit(prices) == expected
