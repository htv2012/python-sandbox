#!/usr/bin/env python


import contextlib


@contextlib.contextmanager
def ignore_exceptions(*exceptions):
    # exceptions = tuple(exceptions)
    try:
        yield
    except exceptions:
        pass


def main():
    li = list(range(3))
    di = dict(a=1, b=2)

    # Ignore one kind of error
    with ignore_exceptions(IndexError):
        print(li[3])

    # Ignore several
    with ignore_exceptions(IndexError, KeyError):
        print(di["c"])

    # Exceptions not ignored will still be raised
    with ignore_exceptions(KeyError):
        print(li[3])


if __name__ == "__main__":
    main()
