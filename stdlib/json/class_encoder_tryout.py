#!/usr/bin/env python
"""Demo: How to JSON a class instance"""

import copy
import json


class classEncoder(json.JSONEncoder):
    """An encoder which works with most classes"""

    def default(self, o):
        if hasattr(o, "__dict__"):
            result = copy.deepcopy(o.__dict__)
            result["__class__"] = o.__class__.__name__
            return result
        return super(self, Book).default(o)


class Book(object):
    """A test object"""

    def __init__(self, title, author, isbn=None):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return "Book(title=%r, author=%r, isbn=%s)" % (
            self.title,
            self.author,
            self.isbn,
        )


def main():
    """Entry"""
    book1 = Book("Nobody's Boy", "Hector Mallot", "978-1298501288")
    print("Original book: {}".format(book1))

    json_string = json.dumps(book1, cls=classEncoder)
    print("Book in JSON format: {}".format(json_string))


if __name__ == "__main__":
    main()
