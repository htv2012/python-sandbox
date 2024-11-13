#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
How does DictReader deal with duplicated columns?
It turns out the last column overwrites the previous ones
"""


import csv


if __name__ == '__main__':
    with open('data.txt') as f:
        for row in csv.DictReader(f):
            print(row)
