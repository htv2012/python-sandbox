#!/usr/bin/env python3
"""
Dataclass allows custom init via __post_init__
"""
import dataclasses


@dataclasses.dataclass
class Book:
    isbn: str
    title: str
    authors: list[str]

    def __post_init__(self):
        print(f"In post init, isbn={self.isbn}")


book = Book("1923232", "Sans Famile", ["Hector Malot"])
print(book)
