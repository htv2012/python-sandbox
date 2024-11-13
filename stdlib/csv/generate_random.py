#!/usr/bin/env python
import csv
import random
import string


def random_row():
    length = random.randint(4, 16)
    name = "".join(random.sample(string.ascii_letters, length))
    number = random.randint(-1000000, 1000000)
    return name, number


def generate(filename, size):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(random_row() for _ in range(size))


if __name__ == "__main__":
    generate("random.csv", 1000000)
