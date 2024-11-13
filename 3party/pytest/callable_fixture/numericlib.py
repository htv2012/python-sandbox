#!/usr/bin/env python3
"""
Numeric-related library
"""
import random


def generate_odd_number() -> int:
    """Generate an odd integer."""
    while True:
        number = random.randint(1, 10000)
        if number % 2 == 1:
            return number
