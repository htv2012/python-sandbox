#!/usr/bin/env python
"""
Module includes tests that are failed, passed, and skipped
"""

import unittest

class ManyOutcomes(unittest.TestCase):
    def test_failed(self):
        self.fail('Out of sugar')

    @unittest.skip('Out of coffee')
    def test_skipped(self):
        pass

    def test_pass(self):
        self.assertEqual(2 + 2, 4)

    def test_skipped_from_inside(self):
        raise unittest.SkipTest('Out of patient')

if __name__ == '__main__':
    unittest.main()
