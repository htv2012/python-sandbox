#!/usr/bin/env python3
"""
Reverse every words in a sentence.

"this is a test" -> "siht  si a tset"
"""
import re


def reverse_every_words(sentence):
    def reverse_word(match: re.Match):
        return match[0][::-1]

    out = re.sub(r"\w+", reverse_word, sentence)
    return out


def main():
    """Entry"""
    samples = [
        "I love my dog",
        "When unsure, try to stay calm.",
        "Keep calm and code in Python",
    ]
    for sentence in samples:
        reversed = reverse_every_words(sentence)
        print(sentence)
        print(reversed)
        print()


if __name__ == "__main__":
    main()
