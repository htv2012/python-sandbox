""" How to I assert list not empty? """
import unittest

NON_EMPTY_LIST = [1, 2]
EMPTY_LIST = []


class ListTest(unittest.TestCase):
    """ How to I assert list not empty? """
    def test_using_empty_list_pass(self):
        """ Recommended """
        self.assertNotEqual([], EMPTY_LIST)

    def test_using_empty_list_fail(self):
        """ Recommended """
        self.assertNotEqual([], NON_EMPTY_LIST)

    def test_using_assert_true_fail(self):
        """ Cryptic, unclear, not recommended """
        self.assertTrue(EMPTY_LIST)

    def test_using_assert_true_pass(self):
        """ Cryptic, unclear, not recommended """
        self.assertTrue(NON_EMPTY_LIST)

if __name__ == '__main__':
    unittest.main()
