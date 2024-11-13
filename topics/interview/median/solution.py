from typing import List


def merge(l1, l2):
    if not l1:
        yield from l2
        return

    if not l2:
        yield from l1
        return

    it1 = iter(l1)
    it2 = iter(l2)
    e1 = next(it1)
    e2 = next(it2)

    # Merge from the 2 lists, until one of the list is exhausted
    while True:
        if e1 < e2:
            yield e1
            try:
                e1 = next(it1)
            except StopIteration:
                yield e2
                yield from it2
                break
        else:
            yield e2
            try:
                e2 = next(it2)
            except StopIteration:
                yield e1
                yield from it1
                break


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_length = len(nums1) + len(nums2)

        # Case: Odd number of elements, return the middle element
        if combined_length % 2 == 1:
            middle = combined_length // 2
            for i, n in enumerate(merge(nums1, nums2)):
                if i == middle:
                    return float(n)

        # Case: Even number of elements, return average
        middle = combined_length // 2 - 1
        it = merge(nums1, nums2)
        for i, n in enumerate(it):
            if i == middle:
                n2 = next(it)
                return (n + n2) / 2.0


print(list(merge([1], [2, 3, 4])))
