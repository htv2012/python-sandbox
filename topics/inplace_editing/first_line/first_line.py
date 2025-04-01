#!/usr/bin/env python

import fileinput
import sys

for line in fileinput.input(sys.argv[1], inplace=1):
    if fileinput.lineno() == 1:
        line += " - modified"
    line = line.replace("$USER", "haiv")
    line = line.replace("$HOME", "/Users/haiv")
    line = line.strip()
    print(line)
