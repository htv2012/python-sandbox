#!/usr/bin/env python3
from hamcrest import *
import unittest


class BiscuitTest(unittest.TestCase):
    def testEquals(self):
        actual = "foo"
        expected = "bar"
        assert_that(actual, equal_to(expected), "Verify the correct name")


if __name__ == '__main__':
    unittest.main()
