import pytest

from numericlib import NumericRange

DEFAULT_SIZE = 3
START_SINGLE = 20001
START_MULTIPLE = 10001


@pytest.fixture(scope="module")
def range_multiple():
    return NumericRange(START_MULTIPLE, count=DEFAULT_SIZE)


@pytest.fixture(scope="module")
def range_single():
    return NumericRange(START_SINGLE, count=1)


def test_range_multiple_convert_to_str(range_multiple):
    assert str(range_multiple) == "10001-10003"


def test_range_multiple_convert_to_list(range_multiple):
    assert list(range_multiple) == [10001, 10002, 10003]


def test_range_multiple_iter(range_multiple):
    count = 0
    for _ in range_multiple:
        count += 1
    assert count == DEFAULT_SIZE


def test_range_single_convert_to_str(range_single):
    assert str(range_single) == str(START_SINGLE)


def test_range_single_convert_to_list(range_single):
    assert list(range_single) == [START_SINGLE]


def test_range_single_iter(range_single):
    count = 0
    for _ in range_single:
        count += 1

    assert count == 1
