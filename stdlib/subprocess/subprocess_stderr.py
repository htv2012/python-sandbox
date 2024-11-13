#!/usr/bin/env python
# encoding: utf-8
"""
subprocess_stderr.py

Created by Hai Vu on 2013-03-10.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import subprocess

if __name__ == '__main__':
    print('\nStart child.sh')
    process = subprocess.Popen(['./child.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_output, stderr_output = process.communicate()

    # Prints stdout
    print("\nOutput:")
    print(stdout_output, end=' ')

    print('\nError:')
    print(stderr_output, end=' ')


