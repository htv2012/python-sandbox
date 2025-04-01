#!/usr/bin/env python3
"""
Generates random tokens
"""

import argparse
import random
import string

VOWES = "aeiouy"
CONSONANTS = [c for c in string.ascii_lowercase if c not in VOWES]
CONSONANTS.extend("br ch cr dr fr gr kn kr ph pr qu sc sch sh th tr wh wr".split())
SYMBOLS = "`!@#$%^&*=+."


def generate_syllable(title_case=True, with_numeric=True, with_symbol=True):
    vowes_count = random.randint(1, 3)
    prefix = random.choice(CONSONANTS)
    suffix = random.sample(VOWES, vowes_count)
    syllable = "".join([prefix] + suffix)
    if title_case:
        syllable = syllable.title()
    if with_numeric and random.choice([True, False]):
        syllable += str(random.randint(0, 99))
    if with_symbol and random.choice([True, False]):
        syllable += random.choice(SYMBOLS)
    return syllable


def generate_password(syllable_count=5, separator="-"):
    token = separator.join(generate_syllable() for _ in range(syllable_count))
    return token


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=0)
    parser.add_argument("-s", "--separator", default="-")
    options = parser.parse_args()

    if options.length != 0:
        password = generate_password(20, separator=options.separator)
        password = password[: options.length]
    else:
        password = generate_password(separator=options.separator)

    print(password)


if __name__ == "__main__":
    main()
