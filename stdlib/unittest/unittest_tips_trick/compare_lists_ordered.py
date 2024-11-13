"""
- Use assertEqual (recommended) or assertListEqual
- Does not work for list of objects
"""
import unittest
from user import User

class MyTestCase(unittest.TestCase):
    # def test_compare_list(self):
    #     self.longMessage = True
    #     actual = [1, 2, 3]
    #     expected = [1,  2, 3]
    #     self.assertEqual(expected, actual, 'Mismatched')

    def test_compare_list_of_objects(self):
        self.longMessage = True
        expected = [User('bob', 501), User('karen', 502)]
        actual = [User('bob', 501), User('alice', 502)]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
