""" Demo the use of longMessage to give more details """

import unittest


class MyTestCase(unittest.TestCase):
    def test_use_long_message(self):
        self.longMessage = True
        actual = 3
        expected = 5
        self.assertEqual(expected, actual, 'Mismatched')

    def test_not_use_long_message(self):
        self.longMessage = False
        actual = 3
        expected = 5
        self.assertEqual(expected, actual, 'Mismatched')

if __name__ == '__main__':
    unittest.main()
