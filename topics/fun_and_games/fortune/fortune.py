#!/usr/bin/env python3
import pathlib
import random

data_file = pathlib.Path(__file__).with_name("fortune.txt")
text = data_file.read_text()
quotes = [quote.strip() for quote in text.split("%")]
quotes = [quote for quote in quotes if quote]
quote = random.choice(quotes)
print(quote)