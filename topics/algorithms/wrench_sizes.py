#!/usr/bin/env python3
"""
Prints some popular wrench sizes
"""

from fractions import Fraction

for i in range(1, 16):
    print(Fraction(i, 16))
