#!/usr/bin/env python
"""
argparse: require both --first and --second or none of them
http://stackoverflow.com/q/40304487/459745
"""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--first')
    parser.add_argument('--second')
    options = parser.parse_args()

    # Error checking
    if (options.first is None) != (options.second is None):
        print('Error: --first and --second must both be supplied or omitted')

    print(options)
