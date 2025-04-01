#!/usr/bin/env python
"""
Use logging to print the exception information
"""

import logging

try:
    a = 59 / (5 - 5)
except ZeroDivisionError:
    logging.exception("Div by zero. Go back to elementary school!")
