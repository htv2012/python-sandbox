"""
Raise from None avoids the problem with having multiple stack traces
"""


def do_work(n):
    try:
        n = int(n)
    except ValueError:
        raise AssertionError(f"Not an integer: {n!r}") from None


def main():
    do_work("hello")


if __name__ == "__main__":
    main()

