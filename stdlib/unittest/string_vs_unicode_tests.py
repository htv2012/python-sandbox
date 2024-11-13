""" Compare string against unicode """

import unittest


class StringVsUnicodeTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual('Mint', u'Mint')


if __name__ == '__main__':
    unittest.main()
