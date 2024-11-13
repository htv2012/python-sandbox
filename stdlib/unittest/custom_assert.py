#!/usr/bin/env python

""" Custom Assert Functions

In some cases, we want a custom function to do the assert, but don't
want to create a subclass of unittest.TestCase to do it. In which cases,
raise unittest.TestCase.failureException to signify a test failure.

Although unittest.TestCase.failureException is the same as
AssertionError, it might not be in the future, so avoid the later.
"""

import unittest


def assertIsOdd(n, message=None):
    if message is None:
        message = "{} is not odd".format(n)

    if n % 2 != 1:
        raise unittest.TestCase.failureException(message)


class CustomAssertions(unittest.TestCase):
    def test1(self):
        n = 4
        assertIsOdd(n)

if __name__ == '__main__':
    unittest.main()
