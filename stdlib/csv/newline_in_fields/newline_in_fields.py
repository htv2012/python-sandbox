#!/usr/bin/env python
import csv


if __name__ == '__main__':
    with open('data.csv') as f:
        for row in csv.DictReader(f):
            print(row)
