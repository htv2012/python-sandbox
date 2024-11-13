#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import json
from pprint import pprint


class Book(object):
    def __init__(self, title, author, isbn=None):
        self.title = title
        self.author = author
        self.isbn = isbn

    @classmethod
    def from_dict(cls, dict_object):
        return cls(
            title=dict_object.get("title"),
            author=dict_object.get("author"),
            isbn=dict_object.get("isbn"),
        )

    def asdict(self):
        return dict(
            title=self.title, author=self.author, isbn=self.isbn, __class__="Book"
        )

    def __str__(self):
        return "{} by {} (isbn: {})".format(self.title, self.author, self.isbn)

    def __repr__(self):
        return "Book(title=%r, author=%r, isbn=%s)" % (
            self.title,
            self.author,
            self.isbn,
        )


if __name__ == "__main__":
    books = [
        Book("Nobody's Boy", "Hector Mallot", "978-1298501288"),
        Book(
            "The AWK Programming Language",
            "Aho, Weinberger, Kernighan",
            "978-0201079814",
        ),
    ]
    print("Original books:")
    pprint(books)

    json_string = json.dumps(
        [book.asdict() for book in books], indent=4, sort_keys=True
    )
    print("\nJSON encoded as:")
    print(json_string)

    books = [Book.from_dict(d) for d in json.loads(json_string)]
    print("\nRound trip:")
    pprint(books)
