#!/usr/bin/env python3
import json
import pathlib


def make_key(word: str) -> str:
    return "".join(sorted(word))


def main():
    """Entry"""
    words_path = pathlib.Path("/usr/share/dict/words")
    assert words_path.exists()

    with open(words_path, "r", encoding="utf-8") as stream:
        content = stream.read().lower()

    anagram = {}
    for word in content.split():
        anagram.setdefault(make_key(word), set()).add(word)

    anagram = {key: sorted(value) for key, value in anagram.items() if value}
    with open("anagrams.json", "w", encoding="utf-8") as stream:
        json.dump(anagram, stream)


if __name__ == "__main__":
    main()
