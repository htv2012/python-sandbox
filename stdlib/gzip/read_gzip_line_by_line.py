#!/usr/bin/env python
from __future__ import print_function
import gzip


if __name__ == '__main__':
    with gzip.open('data.txt.gz', 'rt') as f:
        for line in f:
            print(line, end='')
