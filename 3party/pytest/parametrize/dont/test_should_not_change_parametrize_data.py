"""
According to the doc:

> Parameter values are passed as-is to tests (no copy whatsoever).
> For example, if you pass a list or a dict as a parameter value, and the
> test case code mutates it, the mutations will be reflected in subsequent
> test case calls.

This module demonstrate that.
"""

import pytest

SHARED_LIST1 = [1, 2, 3]
SHARED_LIST2 = [4, 5, 6]


@pytest.mark.parametrize("sequence", [SHARED_LIST1, SHARED_LIST2])
def test_sum(sequence):
    assert sum(sequence) < 100

    # Here is the problem
    sequence[0] = 999


@pytest.mark.parametrize("sequence", [SHARED_LIST1, SHARED_LIST2])
def test_sum2(sequence):
    assert sum(sequence) < 100
