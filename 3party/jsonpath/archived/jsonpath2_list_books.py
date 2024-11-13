#!/usr/bin/env python3
import json
import pathlib

from jsonpath2 import Path

data_path = pathlib.Path(__file__).with_name("books.json")
with open(data_path) as stream:
    store = json.load(stream)

print(f"Welcome to {store['store']}, here are our books:")

# List the books
path = Path.parse_str("$.inventory[*]")
for book in path.match(store):
    book = book.current_value
    print(f"- {book['title']} by {book['author']}")
