#!/usr/bin/env python
import csv
import itertools

def chain_files(*filenames):
    handles = [open(filename) for filename in filenames]
    list(map(next, handles[1:]))
    return itertools.chain(*handles)

if __name__ == '__main__':
    reader = csv.reader(chain_files('data1.csv', 'data2.csv'))
    for row in reader:
        print(row)