#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 2.x csv module cannot handle unicode
"""


import codecs
import csv

if __name__ == "__main__":
    data_filename = "utf8.csv"

    with codecs.open(data_filename, "w", encoding="utf8") as f:
        f.write("Hải,501\n")
        f.write("Tom,502\n")

    with codecs.open(data_filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row, *row)
