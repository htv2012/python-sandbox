#!/usr/bin/env python

import sys
import fileinput


for line in fileinput.input(sys.argv[1], inplace=1):
	line = line.replace('$USER', 'haiv')
	line = line.replace('$HOME', '/Users/haiv')
	line = line.strip()
	print(line)
