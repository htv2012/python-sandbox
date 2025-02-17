""" Compare two lists """

import difflib
import unittest

def compare_lists(list1, list2):
    """ Compare two lists, returns only in 1, only in 2 """
    differ = difflib.Differ()
    diff_result = differ.compare(list1, list2)
    common = []
    only_in_1 = []
    only_in_2 = []
    for item in diff_result:
        if item.startswith('-'):
            only_in_1.append(item)
        elif item.startswith('+'):
            only_in_2.append(item)
        elif item.startswith(' '):
            common.append(item)

    return only_in_1, only_in_2, common


class CompareListsTest(unittest.TestCase):
    def test_1(self):
        only_in_1, only_in_2, common = compare_lists(
            [1, 2, 3, 4], [1, 3, 4, 5])
        self.assertEqual(['- 2'], only_in_1)
        self.assertEqual(['+ 5'], only_in_2)
        self.assertEqual(['  1', '  3', '  4'], common)


if __name__ == '__main__':
    unittest.main()
