#!/usr/bin/env python3
"""
Given a word, find all anagrams of that word.
"""

import argparse
import json

from build import make_key


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs="+")
    options = parser.parse_args()
    return options


if __name__ == "__main__":
    options = parse_command_line()

    with open("anagrams.json", "r", encoding="utf-8") as stream:
        anagrams = json.load(stream)
    for word in options.words:
        print(", ".join(anagrams.get(make_key(word), [word])))
