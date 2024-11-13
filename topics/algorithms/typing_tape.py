#!/usr/bin/env python
"""
whatis: Search a typerwriter tape for text

A typerwriter's tape usually has 3 rows of letters/symbols.  I saw a
forensic show which the police tried to match the contents of a letter
against the typing tape of a suspect's typerwriter. The task was done
by hand and it was tedious. This script should make life easier by
automating that.
"""
import itertools


def make_tape(text):
    tape = [[], [], []]
    for i, c in enumerate(text):
        tape[i % 3].append(c)
    return tape


def decode_tape(tape):
    """Entry"""
    tape = itertools.zip_longest(*tape, fillvalue="")
    tape = itertools.chain(*tape)
    tape = "".join(tape)
    print(tape)


def main():
    tape = make_tape("A typerwriter's tape usually has 3 rows of letters/symbols.")

    print("Tape:")
    for row in tape:
        print(" ".join(row))

    print("\nDecoded:")
    decode_tape(tape)


if __name__ == "__main__":
    main()
