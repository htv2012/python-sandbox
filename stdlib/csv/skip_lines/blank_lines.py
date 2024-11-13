# -*- coding: utf-8 -*-

"""
How do csv readers deal with blank lines?

- csv.reader includes the blank lines
- csv.DictReader does not
"""

import csv

print("")
print("csv.reader and blank lines")
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("")
print("csv.DictReader and blank lines")
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
