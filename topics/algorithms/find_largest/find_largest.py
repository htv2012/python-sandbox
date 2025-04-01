"""
Given a sorted list (smallest to largest) that has been rotated
(direction and number of positions are unknown). Find the value and
index of the largest item.
"""

from itertools import count, tee


def largest(sequence):
    left_items, right_items = tee(sequence)
    next(right_items)

    for index, left_item, right_item in zip(count(), left_items, right_items):
        if left_item > right_item:
            return index, left_item
    return index + 1, next(left_items)


li = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
# li = [5, 7, 8, 9, 10]
print("List: {}".format(li))
print("Largest at index: {}, value: {}".format(*largest(li)))
