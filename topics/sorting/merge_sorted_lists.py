#!/usr/bin/env python3
"""
whatis: How to merge multiple sorted lists into 1
"""

import heapq


def main():
    """Entry"""
    sorted_list1 = [1, 3, 5, 7]
    sorted_list2 = [2, 4, 6]
    sorted_list3 = [8, 9]

    print("# Original sorted lists:")
    print(f"  {sorted_list1}")
    print(f"  {sorted_list2}")
    print(f"  {sorted_list3}")
    print()

    print("# Merge them, while maitaining sorted order:")
    merged_list = list(heapq.merge(sorted_list1, sorted_list2, sorted_list3))
    print(f"  {merged_list}")


if __name__ == "__main__":
    main()
