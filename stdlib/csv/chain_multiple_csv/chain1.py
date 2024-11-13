#!/usr/bin/env python
import csv
import itertools

with open('data1.csv') as f1, open('data2.csv') as f2:
    next(f2)  # Skip header
    reader = csv.reader(itertools.chain(f1, f2))
    for row in reader:
        print(row)
