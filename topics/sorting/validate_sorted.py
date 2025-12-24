"""
whatis: A unittest helper for sorted lists
"""

import unittest


def validate_sorted(sequence):
    for index, (a, b) in enumerate(zip(sequence, sequence[1:])):
        assert a <= b, f"seq={sequence}, unsorted at seq[{index + 1}]={b}"


class SortedTests(unittest.TestCase):
    def test_sorted_list(self):
        validate_sorted([1, 2, 5])

    def test_unsorted_list(self):
        validate_sorted([3, 9, 5])


if __name__ == "__main__":
    unittest.main()
