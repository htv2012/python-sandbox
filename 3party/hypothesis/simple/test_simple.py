#!/usr/bin/env python3
import logging

from hypothesis import given, strategies


@given(strategies.integers())
def test_bin(input_value):
    """Test roundtrip the bin/int functions"""
    logging.debug("input_value=%r", input_value)
    bin_str = bin(input_value)
    round_trip_value = int(bin_str, 2)
    assert round_trip_value == input_value
