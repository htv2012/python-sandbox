import unittest

class MyTestCase(unittest.TestCase):
    def test_use_long_message(self):
        # self.longMessage = True
        actual = [0, 1, 2, 3]
        expected = [0, 1, 2, 4]
        self.assertEqual(expected, actual, 'Mismatched')

if __name__ == '__main__':
    unittest.main()
