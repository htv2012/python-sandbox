"""
Add a method to a class using decorator
"""

import unittest


def add_asserts(cls):
    def assert_odd(self, n, message=None):
        self.assertEqual(1, n % 2, message)

    cls.assert_odd = assert_odd
    return cls


@add_asserts
class MyTest(unittest.TestCase):
    def test_odd(self):
        self.longMessage = True
        n = 4
        self.assert_odd(n, "Number is not odd: {}".format(n))


if __name__ == "__main__":
    unittest.main(verbosity=2)
