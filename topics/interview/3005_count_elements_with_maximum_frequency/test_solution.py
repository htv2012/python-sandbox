import logging
import random

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.maxFrequencyElements


def generate_cases():
    yield pytest.param([1, 2, 2, 3, 1, 4], 4, id="example 1")
    yield pytest.param([1, 2, 3, 4, 5], 5, id="example 2")
    yield pytest.param([], 0, id="len=0")
    yield pytest.param([9], 1, id="len=1")
    yield pytest.param([2, 2, 2, 2, 2], 5, id="same element")

    for _ in range(10):
        unique_count = random.randint(3, 5)
        freq = {i: random.randint(1, 20) for i in range(unique_count)}
        max_freq = max(freq.values())
        expected = sum(value for value in freq.values() if value == max_freq)
        nums = []
        for number, count in freq.items():
            nums.extend([number] * count)
        random.shuffle(nums)
        yield pytest.param(nums, expected, id=f"{expected=}")


@pytest.mark.parametrize("nums, expected", generate_cases())
def test_solution(nums, expected, fut):
    logging.debug("nums=%r", nums)
    logging.debug("expected=%r", expected)
    assert fut(nums) == expected
