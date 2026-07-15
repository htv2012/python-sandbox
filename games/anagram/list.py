#!/usr/bin/env python3
"""List anagrams"""

import argparse
import json


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lower", type=int, default="2")
    options = parser.parse_args()

    with open("anagrams.json", "r", encoding="utf-8") as stream:
        anagrams = json.load(stream)

    found = sorted(words for words in anagrams.values() if options.lower <= len(words))
    for words in found:
        print(", ".join(words))


if __name__ == "__main__":
    main()
