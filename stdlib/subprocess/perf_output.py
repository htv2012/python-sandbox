#!/usr/bin/env python
# encoding: utf-8

import subprocess

if __name__ == '__main__':
    cmd = "perf stat -e cache-misses echo stdout"
    cmd = ['ls', '-1', '*']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_output, stderr_output = process.communicate()

    print("\nOutput:")
    print(stdout_output, end=' ')

    print('\nError:')
    print(stderr_output, end=' ')


