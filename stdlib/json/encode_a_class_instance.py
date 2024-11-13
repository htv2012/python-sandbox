#!/usr/bin/env python
"""Demo: How to JSON a class instance"""

import collections.abc
import json


class Book(object):
    """A test object"""

    def __init__(self, title, author, isbn=None):
        self.title = title
        self.author = author
        self.isbn = isbn

    @classmethod
    def from_dict(cls, dict_object):
        """Turns a dictionary into a Book"""
        return cls(
            title=dict_object.get("title"),
            author=dict_object.get("author"),
            isbn=dict_object.get("isbn"),
        )

    def __str__(self):
        return "{} by {} (isbn: {})".format(self.title, self.author, self.isbn)

    def __repr__(self):
        return "Book(title=%r, author=%r, isbn=%s)" % (
            self.title,
            self.author,
            self.isbn,
        )


class BookEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Book):
            return dict(__class__="Book", title=o.title, author=o.author, isbn=o.isbn)
        return super(self, Book).default(o)


class BookDecoder(json.JSONDecoder):
    def decode(self, encoded_string):
        new_object = json.loads(encoded_string)

        if (
            isinstance(new_object, collections.abc.Mapping)
            and new_object.get("__class__") == "Book"
        ):
            return Book.from_dict(new_object)
        return super().decode(encoded_string)


def main():
    """Entry"""
    book1 = Book("Nobody's Boy", "Hector Mallot", "978-1298501288")
    print("Original book: {}".format(book1))

    json_string = json.dumps(book1, cls=BookEncoder)
    print("Book in JSON format: {}".format(json_string))

    book2 = json.loads(json_string, cls=BookDecoder)
    print("Book in round trip: {}".format(book2))

    print("\n---\n")

    my_list = [book1, 15, "hello"]
    print("Original: {}".format(my_list))

    json_string = json.dumps(my_list, cls=BookEncoder)
    print("Encoded: {!r}".format(json_string))

    new_list = json.loads(json_string, cls=BookDecoder)
    print("Round trip: {}".format(new_list))


if __name__ == "__main__":
    main()
