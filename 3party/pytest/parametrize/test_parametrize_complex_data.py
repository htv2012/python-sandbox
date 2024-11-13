#!/usr/bin/env python3
"""
Parameterize tests with complex data using factory function and
SimpleNamespace combination.
"""
import types

import pytest


def make_input(id, marks=None, **kwargs):
    """Return a test input object with id, so pytest can customize names."""
    data = types.SimpleNamespace(**kwargs)
    return pytest.param(data, marks=marks or tuple(), id=id)


TEST_INPUT = [
    make_input(id="base 2", input_value="10", base=2, expected=2),
    make_input(id="base 8", input_value="100", base=8, expected=64),
]


@pytest.mark.parametrize("data", TEST_INPUT)
def test_using_factory(data):
    assert int(data.input_value, data.base) == data.expected
