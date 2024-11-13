#!/usr/bin/env python
"""
Explores ways to fail a test.
"""

import unittest


class WithoutYou(unittest.TestCase.failureException):
    pass


class NoMilkToday(AssertionError):
    pass


class WaysToFail(unittest.TestCase):
    def test_using_fail(self):
        self.fail('Fail explicitly')

    def test_subclass_of_failure_exception(self):
        raise WithoutYou('Harry Nilsson')

    def test_subclass_of_assertion_error(self):
        raise NoMilkToday("Herman's Hermits")

    def test_assert_exception(self):
        raise AssertionError('This is a failure, not error')

    def test_failure_exception(self):
        raise unittest.TestCase.failureException('failureException')

    def test_assert(self):
        assert 3 == 5

    def test_error(self):
        raise ValueError('This must be an error')


if __name__ == '__main__':
    unittest.main()
