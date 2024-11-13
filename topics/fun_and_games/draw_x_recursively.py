#!/usr/bin/env python3
"""
Draw X recursively
https://stackoverflow.com/q/70904352/459745
"""

def draw_x(gap=5, indent=0):
    """
    Draws the letter X, `gap` is the number of spaces between the
    first and last asterisk and `indent` is the number of spaces
    before the first asterisk.
    """
    prefix = indent * " "
    if gap < 1:
        print(f"{prefix}*")
        return
    print(f"{prefix}*{gap*' '}*")
    draw_x(gap - 2, indent+1)
    print(f"{prefix}*{gap*' '}*")


def main():
    """ Entry """
    draw_x()


if __name__ == "__main__":
    main()

