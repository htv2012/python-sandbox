#!/usr/bin/env python
"""
Tests the OneBasedTuple
"""

import pytest

from one_based import OneBasedTuple

SAMPLE = OneBasedTuple.from_iterable(
    "one two three four five six seven eight nine ten".split()
)


def test_first():
    assert SAMPLE[1] == "one"


def test_last():
    assert SAMPLE[10] == "ten"


def test_negative_index():
    assert SAMPLE[-1] == "ten"


def test_negative_index2():
    assert SAMPLE[-2] == "nine"


def test_out_of_range_lower_bound():
    with pytest.raises(IndexError):
        SAMPLE[0]


def test_out_of_range_upper_bound():
    with pytest.raises(IndexError):
        SAMPLE[11]


def test_loop():
    for index, element in enumerate(SAMPLE):
        if index == 0:
            assert element == "one"
        elif index == 9:
            assert element == "ten"


def test_slice():
    assert SAMPLE[1:4] == ("one", "two", "three")


def test_slice_backward():
    assert SAMPLE[-1:-3:-1] == ("ten", "nine")


def test_slice_with_step():
    assert SAMPLE[1:5:2] == ("one", "three")
