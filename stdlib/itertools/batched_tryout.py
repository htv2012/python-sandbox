#!/usr/bin/env python3
"""
itertools.batched demo
"""

import itertools


def main():
    """Entry"""
    # raw_data: each record consists of 3 fields, but were assembled
    # without any boundary
    raw_data = "501 john zsh 502 karen bash".split()
    print("\n# Raw Data")
    print(raw_data)

    # Convert raw data into 3-field records
    print("\n# Converted")
    print(list(itertools.batched(raw_data, 3)))


if __name__ == "__main__":
    main()
