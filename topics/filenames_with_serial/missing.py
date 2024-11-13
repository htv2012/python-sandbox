#!/usr/bin/env python
# encoding: utf-8
'''
missing.py

Created by Hai Vu on 2013-03-29.
Copyright (c) 2013 High View Software. All rights reserved.

Find missing integers in a sequence

'''

def find_missing_items(int_list):
    '''
    Finds missing integer within an unsorted list and return a list of 
    missing items
    
    >>> find_missing_items([1, 2, 5, 6, 7, 10])
    [3, 4, 8, 9]
    
    >>> find_missing_items([3, 1, 2])
    []
    '''

    # Put the list in a set, find smallest and largest items
    original_set  = set(int_list)
    smallest_item = min(original_set)
    largest_item  = max(original_set)
    
    # Create a super set of all items from smallest to largest
    full_set = set(range(smallest_item, largest_item + 1))
    
    # Missing items are the ones that are in the full_set, but not in
    # the original_set
    return sorted(full_set - original_set)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
