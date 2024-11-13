#!/usr/bin/env python

"""
Use bisect to start and maintain a sorted list
"""


import bisect

ordered_list = [2, 4]
print("Before insertion:", ordered_list)

bisect.insort(ordered_list, 5)
bisect.insort(ordered_list, 3)
bisect.insort(ordered_list, 1)

print("After insertion: ", ordered_list)
