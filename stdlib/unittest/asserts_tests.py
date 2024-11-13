#!/usr/bin/env python
"""
Explores different asserts
"""

import unittest


class KindsOfAsserts(unittest.TestCase):
    def setUp(self):
        self.list1 = [1, 2, 3]
        self.list2 = [1, 3, 2]
        self.tuple1 = (2, 2, 3)
        self.tuple2 = (3, 2, 2)

    def test_list_equal(self):
        """ Compare two lists, order matters """
        self.assertListEqual(self.list1, self.list2)

    def test_sets_equal(self):
        set1 = {1, 2, 3}
        set2 = {1, 3, 2}
        self.assertEqual(set1, set2)

    def test_set_against_list(self):
        set1 = {1, 3, 2}
        list1 = [1, 2, 3]
        self.assertItemsEqual(list1, set1)

        set2 = {'foo', u'bar'}
        list2 = ['bar', 'foo']
        self.assertItemsEqual(list2, set2)

    def test_items_equal(self):
        """ Compare two iterables, order does not matter """
        self.assertItemsEqual(self.list1, self.list2)
        self.assertItemsEqual(self.tuple1, self.tuple2)

    def test_belong(self):
        self.assertIn(5, self.list1, "Johnny 5 not found")

if __name__ == '__main__':
    unittest.main(verbosity=2)
