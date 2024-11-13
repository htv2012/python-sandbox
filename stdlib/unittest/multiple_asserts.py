#!/usr/bin/env python
"""
Does multiple assert work?
"""

import unittest

class MultipleAsserts(unittest.TestCase):
    def test_multiple_asserts(self):
        """ Multiple assert: no! Assert will exits test """
        x = 5
        self.assertEqual(2, x)
        print 'intermission'
        self.assertEqual(3, x)

if __name__ == '__main__':
    unittest.main(verbosity=2)