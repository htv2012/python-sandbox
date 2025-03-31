#!/usr/bin/env python

"""
I want to make a word lock which has 5 columns. Each columns can have 10
letters. How do I determine which letter to place in each column?
http://www.wordlock.com/
"""

from collections import Counter


def create_columns(columns_count):
    """
    Create columns for a word lock
    """
    # Create counters for each of the columns
    counters = [Counter() for _ in range(columns_count)]

    with open("/usr/share/dict/words") as file_handle:
        words = file_handle.read().split()

    # Count the letters
    for word in words:
        word_length = len(word)
        if word_length < 4 or word_length > columns_count:
            continue
        word = word.upper()

        for counter, letter in zip(counters, word):
            counter.update(letter)

    # Pick out the most frequently used letters
    columns = []
    for counter in counters:
        letters = [letter for letter, frequency in counter.most_common(10)]
        columns.append(letters)

    # Replace the last column, last letter with a space
    columns[-1][-1] = " "

    return columns


def show(columns):
    """
    Shows the columns
    """
    columns_count = len(columns)
    print("WORD LOCK")
    print(" ".join(str(i) for i in range(1, columns_count + 1)))
    print("-" * columns_count * 2)
    for row in zip(*columns):
        print(" ".join(row))


def main():
    """Entry"""
    columns = create_columns(5)
    show(columns)


if __name__ == "__main__":
    main()
