#!/usr/bin/env python3
from numericlib import generate_odd_number


def test_odd():
    """Test using function call."""
    number = generate_odd_number()
    assert number % 2 == 1


def test_odd_using_fixture(odd_number):
    """Test using fixture."""
    assert odd_number % 2 == 1
