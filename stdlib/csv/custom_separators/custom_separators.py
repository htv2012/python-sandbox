#!/usr/bin/env python
# -*- coding: utf-8 -*-


import codecs
import csv


if __name__ == '__main__':
    with codecs.open('data.txt', encoding='utf-8') as f:
        csvreader = csv.reader(f, delimiter='|')
        for line in csvreader:
            print(line)
