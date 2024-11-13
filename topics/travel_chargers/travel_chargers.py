#!/usr/bin/env python3
"""Catalog the travel chargers and cables needed."""
import argparse
import collections
import csv
import pathlib


parser = argparse.ArgumentParser()
parser.add_argument("person", nargs="*")
options = parser.parse_args()

cables_count = collections.defaultdict(int)
chargers_count = collections.defaultdict(int)

data_path = pathlib.Path(__file__).with_name("data.csv")
with open(data_path) as stream:
    next(stream)  # Skip headers
    reader = csv.reader(stream)

    for person, device, cable, charger in reader:
        if not options.person or person in options.person:
            print(f"name: {person}, device: {device}, cable: {cable}, charger: {charger}")
            cables_count[cable] += 1
            chargers_count[charger] += 1

print()
print("PEOPLE")
for person in options.person:
    print(f"- {person}")
print()

print("CABLES")
for name, count in cables_count.items():
    print(f"{count:>2} {name}")

print()
print("CHARGERS")
for name, count in chargers_count.items():
    print(f"{count:>2} {name}")

