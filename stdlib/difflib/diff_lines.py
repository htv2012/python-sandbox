#!/usr/bin/env python
"""
"""

import difflib


EXPECTED = """
0000000 07 00 00 00 20 00 00 00 00 00 00 00 00 00 00 00
0000020 00 00 00 00 00 00 00 00 41 31 31 38 00 00 00 00
0000040 00 00 00 00 00 00 00 00 00 00 00 00 41 31 31 38
0000060 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000100 50 43 41 2d 30 34 33 36 2d 30 30 20 52 45 56 20
0000120 32 37 00 00 70 63 61 30 34 33 36 6d 30 30 31 37
0000140 00 00 00 00 00 00 00 00 34 30 30 2d 30 30 38 36
0000160 2d 30 30 20 52 45 56 20 31 00 00 00 78 78 2d 61
0000200 62 63 64 2d 32 38 37 36 00 00 00 00 00 00 00 00
0000220 51 64 01 10 23 00 46 00 08 51 36 33 36 39 37 30
0000240 04 00 00 00 61 00 04 00 50 31 2e 30 00 00 00 00
0000260 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000300 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000320 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000340 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000360 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000400 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000420 00 00 00 00 00 00 00 00 02 01 00 00 49 46 58 00
0000440 53 4c 42 39 36 37 30 00 00 00 00 00 00 00 00 00
0000460 55 00 07 00 00 cb 11 00 00 00 00 00 0a 00 b0 69
0000500 00 00 00 00
0000504
""".strip()

ACTUAL = """
0000000 07 00 00 00 20 00 00 00 00 00 00 00 00 00 00 00
0000020 10 00 00 00 00 00 00 00 41 31 31 38 00 00 00 00
0000040 00 00 00 00 00 00 00 00 00 00 00 00 41 31 31 38
0000060 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000100 50 43 41 2d 30 34 33 36 2d 30 30 20 52 45 56 20
0000120 32 37 00 00 70 63 61 30 34 33 36 6d 30 30 31 37
0000140 00 00 00 99 00 00 00 XX 34 30 30 2d 30 30 38 36
0000160 2d 30 30 20 52 45 56 20 31 00 00 00 78 78 2d 61
0000200 62 63 64 2d 32 38 37 36 00 00 00 00 00 00 00 00
0000220 51 64 01 10 23 00 46 00 08 51 36 33 36 39 37 30
0000240 04 00 00 00 61 00 04 00 50 31 2e 30 00 00 00 00
0000260 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000300 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000320 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000340 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000360 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000400 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000420 00 00 00 00 00 00 00 00 02 01 00 00 49 46 58 00
0000440 53 4c 42 39 36 37 30 00 00 00 00 00 00 00 00 00
0000460 55 00 07 00 00 cb 11 00 00 00 00 00 0a 00 b0 69
0000500 00 00 00 00
0000504
""".strip()


def compare_lines(text1, text2):
    """
    Compare two multi-line blocks of text and return the differences. If
    the two blocks are identical, then the function will return an empty
    string. If they differ, the function will return a multi-line block
    of text similar to the output of the diff command.

    :param text1: The first block of text
    :param text2: The second block of text
    :return: An empty string if the two are identical, or a diff output
        if they differ
    """
    text1 = text1.splitlines()
    text2 = text2.splitlines()

    differ = difflib.Differ()
    diff = list(differ.compare(text1, text2))

    if any(line.startswith('?') for line in diff):
        return '\n'.join(diff)
    return ''


def main():
    """ Entry """
    print(compare_lines(EXPECTED, EXPECTED) or 'IDENTICAL')
    print('=' * 80)
    print(compare_lines(EXPECTED, ACTUAL) or 'IDENTICAL')


if __name__ == '__main__':
    main()
