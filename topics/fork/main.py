#!/usr/bin/env python3
"""
Demo: How to use os.fork()
"""
import os, sys


def main():
    print("In main.py, pid=%d" % os.getpid())
    pid = os.fork()

    if pid != 0:
        print(f"Still in main, child pid is {pid}")
        return

    print('I am the child process, pid=%d' % os.getpid())

if __name__ == "__main__":
    main()
