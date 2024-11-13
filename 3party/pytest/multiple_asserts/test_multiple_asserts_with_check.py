import pytest_check
from pytest_check import check


def test_example():
    a = 1
    b = 2
    c = [2, 4, 6]
    x = True

    pytest_check.equal(a, b)
    pytest_check.not_equal(a, b)
    pytest_check.is_(a, b)
    pytest_check.is_not(a, b)
    pytest_check.is_true(x)
    pytest_check.is_false(x)
    pytest_check.is_none(x)
    pytest_check.is_not_none(x)
    pytest_check.is_in(a, c)
    pytest_check.is_not_in(b, c)
    pytest_check.is_instance(a, str)
    pytest_check.is_not_instance(a, str)
    pytest_check.almost_equal
    pytest_check.not_almost_equal
    pytest_check.greater(a, b)
    pytest_check.greater_equal(a, b)
    pytest_check.less(a, b)
    pytest_check.less_equal(a, b)

def test_example2():
    actual = {
            "name": "Jason",
            "age": 29,
            }
    with check:
        assert actual["name"] == "John"
    with check:
        assert actual["age"] == 30

def test_multiple_raises():
    with pytest_check.raises(IndexError):
        pass

    with pytest_check.raises(KeyError):
        pass
