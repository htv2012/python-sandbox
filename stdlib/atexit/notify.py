#!/usr/bin/env python
import sys

print('enter notify')
if sys.argv[1] == '0':
    print('Success')
else:
    print('Failed with code', sys.argv[1])

print('exit notify')