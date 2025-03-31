#!/usr/bin/env python3
import itertools
import sys

# Phone buttons
button = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

with open("/usr/share/dict/words") as stream:
    dictionary = set(word.lower() for word in stream.read().split())

for word in [
    "6673",
    "8426",
    "4253",
    "2",
    "6455466",
    "3447",
    "9373",
    "443336",
    "46",
    "843",
    "96753'7",
    "5274378",
    "327837",
    "344",
    "4868",
]:
    candidates = [
        "".join(c)
        for c in itertools.product(*[button.get(x, x) for x in word])
        if "".join(c) in dictionary
    ]
    print(f"{word}: {candidates}")
