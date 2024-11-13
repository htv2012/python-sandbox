"""
- Use assertItemsEqual
- Does not work for list of objects
"""
import unittest

class MyTestCase(unittest.TestCase):
    def test_use_long_message(self):
        self.longMessage = True
        actual = [1, 2, 3]
        expected = [3, 1, 2]
        self.assertItemsEqual(expected, actual, 'Mismatched')

if __name__ == '__main__':
    unittest.main()
