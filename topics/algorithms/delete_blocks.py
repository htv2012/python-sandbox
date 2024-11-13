#!/usr/bin/env python3
"""
Demo: Delete blocks of data from a sequence
Created on Tue Dec  8 06:05:52 2015

@author: hvu
"""


def delete_blocks(iterable, blocks):
    exclude = set()
    for block in blocks:
        try:
            exclude.update(list(range(*block)))
        except TypeError:
            exclude.add(block)
    return [cell for i, cell in enumerate(iterable) if i not in exclude]


def delete_substring_blocks(s, blocks):
    return "".join(delete_blocks(s, blocks))


def main():
    """Entry"""
    # Try it out
    test_string = "0123456789abc"
    blocks = [(5, 7), (2, 4), 8, 10]
    result = delete_substring_blocks(test_string, blocks)

    print("Before: {!r}".format(test_string))
    print("Blocks:", blocks)
    print("After: {!r}".format(result))

    print("---")
    li = list(range(20))
    blocks = [(1, 5), 10, (15, 17)]
    print(f"Before: {li}")
    print(f"Blocks: {blocks}")
    after = delete_blocks(li, blocks)
    print(f"After: {after}")


if __name__ == "__main__":
    main()
