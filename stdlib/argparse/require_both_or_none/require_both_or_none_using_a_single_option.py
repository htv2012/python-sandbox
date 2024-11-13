#!/usr/bin/env python
"""
argparse: require both --first and --second or none of them
http://stackoverflow.com/q/40304487/459745
"""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--first-and-second', nargs=2)
    options = parser.parse_args()

    print(options)
