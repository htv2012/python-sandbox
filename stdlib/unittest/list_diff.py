from collections import Counter
import unittest


def unordered_list_diff(list1, list2):
    """ Disregard of items order, compare two lists.
    :param list1: List to compare
    :param list2: List to compare
    :return: None if the lists are identical, or a tuple of 3:
        Items only in list 1 or None
        Items only in list 2 or None
        [[item, list1-count, list2-count], ...]] or None
    Examples:
    >>> unordered_list_diff([1,2,3], [1,2,3]) # Identical lists returns None
    >>> unordered_list_diff([1,2,3], [1,2]) # list1 has extra item
    ([3], None, None)
    >>> unordered_list_diff([1,2], [1,2,3]) # list2 has extra item
    (None, [3], None)
    >>> unordered_list_diff([1,2,2,3], [1,2,3,3]) # Different counts of items
    (None, None, [[2, 2, 1], [3, 1, 2]])
    """
    # Check for identical lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    if counter1 == counter2:
        return None

    # Find list of items that are different and common
    key_set1 = set(list1)
    key_set2 = set(list2)
    only_in_1 = list(key_set1 - key_set2) or None
    only_in_2 = list(key_set2 - key_set1) or None
    common_keys = key_set1 & key_set2 or None

    # Create a list of items that are common, but with different counts
    if common_keys is not None:
        items_diff = [[k, counter1[k], counter2[k]] for k in common_keys if counter1[k] != counter2[k]] or None

    return only_in_1, only_in_2, items_diff


class CompareListTest(unittest.TestCase):
    def test_identical_lists(self):
        self.assertIsNone(unordered_list_diff(
            [7, 8, 9], [7, 8, 9]))

    def test_same_items_but_different_order(self):
        self.assertIsNone(unordered_list_diff(
            [7, 8, 9], [8, 7, 9]))

    def test_list1_has_extra(self):
        only_in_1, only_in_2, items_diff = unordered_list_diff(
            [7, 8, 9], [7, 9])
        self.assertEqual([8], only_in_1)
        self.assertIsNone(only_in_2)
        self.assertIsNone(items_diff)

    def test_list2_has_extra(self):
        only_in_1, only_in_2, items_diff = unordered_list_diff(
            [7, 8], [7, 9, 8])
        self.assertIsNone(only_in_1)
        self.assertEqual([9], only_in_2)
        self.assertIsNone(items_diff)

    def test_lists_have_same_items_but_different_count(self):
        only_in_1, only_in_2, items_diff = unordered_list_diff(
            [7, 9, 9, 8], [8, 8, 7, 9])
        self.assertIsNone(only_in_1)
        self.assertIsNone(only_in_2)
        self.assertItemsEqual([[8, 1, 2], [9, 2, 1]], items_diff)

    def test_list_not_empty(self):
        actual = [1, 2]
        self.assertNotEqual([], actual)

if __name__ == '__main__':
    unittest.main()
