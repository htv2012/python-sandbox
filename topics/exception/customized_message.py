"""Customize an exception's message"""

import sys

try:
    a = 59 / (5 - 5)
except ZeroDivisionError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("Old message: {}".format(exc_value))
    exc_value = "Div by zero, dude!"
    raise exc_type(exc_value).with_traceback(exc_tb)
