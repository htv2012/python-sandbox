#!/usr/bin/env python
"""
Module includes tests that are failed, passed, and skipped
"""

import unittest


class TestSomething(unittest.TestCase):
    def test_water(self):
        self.assertTrue(3 > 2)

    @unittest.expectedFailure
    def test_ice(self):
        self.assertTrue(2 - 2)

    def test_sugar(self):
        self.fail('Out of sugar')

    @unittest.skip('Out of coffee')
    def test_coffee(self):
        self.assertTrue(3 > 2)

    @unittest.skipIf(True, 'Out of cream')
    def test_cream(self):
        self.assertTrue(3 > 2)

    @unittest.skip('Out of' + ' salt')
    def test_salt(self):
        pass


class BaseTest(unittest.TestCase):
    pass


@unittest.skip
class TestOtherThings(BaseTest):
    def _helper(self):
        pass

    def test_other_coffee(self):
        pass


@unittest.skipIf(True, 'Beat it')
class TestMoreStuff(unittest.TestCase):
    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main()
