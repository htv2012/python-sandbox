"""Test both the return value and the exception.

Normally, we create happy-path test cases and error cases as two
separate tests. In this module, we introduce the `get_exception_and_return`
function, which allows us to test both sets of test cases in the
same function.
"""

import pytest


def get_exception_and_return(func, *args, **kwargs):
    """Call a function and return both the exception type and the return value.

    :param func: The function to call
    :param args: The positional arguments
    :param kwargs: The keyword arguments
    :return: (exception type, and return value). If the call does
        not generate an exception then return (None, value). If the
        call generate an exception, return (exception type, None).
    """
    try:
        return None, func(*args, **kwargs)
    except Exception as error:
        return error, None


def my_div(a, b):
    """Code under test."""
    div_value = a // b
    return div_value


@pytest.mark.parametrize(
    "a, b, expected_exception_type, expected_return",
    [
        pytest.param(11, 2, type(None), 5, id="Happy Path"),
        pytest.param(10, 0, ZeroDivisionError, None, id="Divide by Zero"),
        pytest.param("5", 2, TypeError, None, id="Not a Number"),
    ],
)
def test_div_and_mod(a, b, expected_exception_type, expected_return):
    actual_exception, actual_result = get_exception_and_return(my_div, a, b)
    assert isinstance(actual_exception, expected_exception_type)
    assert actual_result == expected_return

