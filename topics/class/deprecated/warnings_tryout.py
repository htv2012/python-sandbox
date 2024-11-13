#!/usr/bin/env python3
import warnings


class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title!r})"

    @classmethod
    def make(cls, title):
        warnings.warn("Deprecate, use __init__", DeprecationWarning)
        return cls(title)


def main():
    # Turns on warnings
    # https://docs.python.org/3.6/library/warnings.html#warning-filter
    warnings.simplefilter("default")

    # See warning
    book = Book.make("Sans Famille")
    print(book)

    # Don't see warning
    book2 = Book("Playing for Pizza")
    print(book2)


if __name__ == "__main__":
    main()
