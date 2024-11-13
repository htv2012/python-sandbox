#!/usr/bin/env python

import shlex


def try_split():
    print("#\n# Split Demo\n#\n")
    sample = [
        ('abcd xvc  23432 "exampe" 366', {}),
        ('abcd xvc  23432 "exampe" 366', {"posix": False}),
        ("one two three # This is a comment", {}),
        ("one two three # This is a comment", {"comments": True}),
    ]

    for text, kwargs in sample:
        print(f">>> split({text!r}", end="")
        if kwargs:
            print(", ", end="")
            print(", ".join(f"{k}={v!r}" for k, v in kwargs.items()), end="")
        print(")")

        out = shlex.split(text, **kwargs)
        print(out)
        print()


def try_join():
    print("#\n# Join Demo\n#\n")

    samples = [
        ["one", "two", "three"],
        ["one", "two", "number three"],
    ]

    for sequence in samples:
        print(f">>> join({sequence!r})")
        out = shlex.join(sequence)
        print(out)
        print()


def main():
    """Entry"""
    try_split()
    try_join()


if __name__ == "__main__":
    main()
