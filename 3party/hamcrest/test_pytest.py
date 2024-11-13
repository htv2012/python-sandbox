#!/usr/bin/env python3
"""
Demo: Use of hamcrest with pytest
"""
from hamcrest import *


def test_simple():
    assert_that(5, equal_to(5), "Verify numbers are the same")
