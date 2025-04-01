"""
Tests the const.define() function
"""

import pytest

import const


@pytest.fixture
def myconst():
    constants = const.define(HLS=101, DASH=102)
    return constants


def test_values(myconst):
    assert myconst.HLS == 101
    assert myconst.DASH == 102


def test_number_of_values(myconst):
    assert len(myconst) == 2


def test_immunity(myconst):
    with pytest.raises(AttributeError):
        myconst.HLS = 1


def test_iter(myconst):
    assert list(myconst) == [101, 102]
