#!/usr/bin/env python3

import pytest

from numericlib import generate_odd_number

# This fixture is the same as generate_odd_number
# So if we need a function, use generate_odd_number,
# and if we need a fixture, use odd_number.
odd_number = pytest.fixture(generate_odd_number)
