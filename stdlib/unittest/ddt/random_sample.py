#!/usr/bin/env python
"""
Problem
=======
You have too many test cases, so only want to run a subset of
these test cases at a time.

Solution
========
Use `random.sample` to pick out the subset and pass that subset to
`ddt.data`
"""

import unittest
import ddt
import random


@ddt.ddt
class MyTestCase(unittest.TestCase):
    all_test_cases = [1, 8, 10, 12, 2, 4, 6]

    @ddt.data(*random.sample(all_test_cases, 2))
    def test_even_number(self, number):
        self.assertEqual(
            0,
            number % 2,
            'Number is not even: {}'.format(number))


if __name__ == '__main__':
    unittest.main()
