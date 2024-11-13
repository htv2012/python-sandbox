#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
How does DictReader deal with duplicated columns?
It turns out the last column overwrites the previous ones
We can use this fact to remove duplicate columns
"""

from __future__ import print_function
import csv


if __name__ == '__main__':
    with open('data.csv') as f, open('remove_duplicated_columns_using_dict_reader.csv', 'wb') as outfile:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(outfile, reader.)
            print(row)
