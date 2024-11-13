"""
1. Should implement __repr__
2. Must implement __eq__
"""
import unittest
from user import User

class MyTestCase(unittest.TestCase):
    def test_compare_objects(self):
        self.longMessage = True
        expected = User('bob', uid=501)
        actual = User('bob', uid=501)
        self.assertEqual(expected, actual, 'Mismatched')

if __name__ == '__main__':
    unittest.main()
