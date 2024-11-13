#!/usr/bin/env python
"""
class-level vars
"""

import unittest


class MyTest(unittest.TestCase):
    name_var = __name__

    def test_name_var(self):
        self.assertEqual('__main__', self.name_var)

if __name__ == '__main__':
    unittest.main()
