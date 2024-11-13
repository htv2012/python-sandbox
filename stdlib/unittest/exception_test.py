#!/usr/bin/env python
""" Test that raise assertion """

import unittest


class AssertionTest(unittest.TestCase):
    def test_that_raise_exception(self):
        """ Test that will raise assertion """
        with self.assertRaises(ValueError):
            number = int('99 beers on the wall')


if __name__ == '__main__':
    unittest.main()
