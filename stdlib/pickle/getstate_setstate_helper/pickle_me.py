#!/usr/bin/env python3
import io
import pickle

import persistence


@persistence.serializable("title", "author")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"


def main():
    """ Entry """

    # Original object
    book = Book("Sans Famille", "Hector Malot")
    print(f"\nOriginal:\n{book}")

    # Save state
    buffer = io.BytesIO()
    pickle.dump(book, buffer)

    # Load state
    buffer.seek(0)
    book2 = pickle.load(buffer)
    print(f"\nNew:\n{book2}")


if __name__ == '__main__':
    main()
