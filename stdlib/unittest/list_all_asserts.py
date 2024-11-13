# encoding: utf-8

import unittest

class AssertsTest(unittest.TestCase):
    def test_list_all_asserts(self):
        print '\n'.join(m for m in dir(self) if m.startswith('assert'))

if __name__ == '__main__':
    unittest.main(verbosity=2)