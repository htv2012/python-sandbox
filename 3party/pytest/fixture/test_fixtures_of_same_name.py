"""Fixtures cannot have same name."""

import pytest


@pytest.fixture
def test_data():
    """Define data for test1."""
    return "data1"


def test1(test_data):
    assert test_data == "data1"


@pytest.fixture
def test_data2():
    """Define data for test2."""
    return "data2"


def test2(test_data2):
    assert test_data2 == "data2"
