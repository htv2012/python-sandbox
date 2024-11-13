#!/usr/bin/env python
import csv
import itertools

def chain_files(*filenames):
    for count, filename in enumerate(filenames):
        with open(filename) as f:
            if count > 0:
                next(f)

            for line  in  f:
                yield line


if __name__ == '__main__':
    reader = csv.reader(chain_files('data1.csv', 'data2.csv'))
    for row in reader:
        print(row)