"""
Deals with serial text
"""

import argparse
import re


def bump(text: str, delta: int = 1):
    """
    Return the next string in the sequence

    >>> bump('edit 125')
    'edit 126'

    >>> bump('edit 125', -1)
    'edit 124'
    """

    def _replace(match: re.Match):
        nonlocal delta
        number = int(match[0]) + delta
        return str(number)

    return re.sub(r"\d+", _replace, text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--inc",
        type=int,
        metavar="N",
        dest="delta",
        default=1,
        help="Increase by N",
    )
    parser.add_argument(
        "-d",
        "--dec",
        type=lambda x: -int(x),
        dest="delta",
        metavar="N",
        help="Decrease by N",
    )
    parser.add_argument("text", nargs="+")
    options = parser.parse_args()

    text = " ".join(options.text)
    out = bump(text, delta=options.delta)
    print(out)


if __name__ == "__main__":
    main()
