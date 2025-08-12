#!/usr/bin/env python3

from one_based import OneBasedTuple

tup = OneBasedTuple("Anna", "Benny", "Cameron")

print("\n# Tuple")
print(f"{tup=}")
print(f"{len(tup)=}")

print("\n# Indices")
print(f"{tup[1]=}")
print(f"{tup[2]=}")
print(f"{tup[3]=}")

print("\n# Negative Indices")
print(f"{tup[-1]=}")
print(f"{tup[-2]=}")
print(f"{tup[-3]=}")

print("\n# Slices")
print(f"{tup[1:3]=}")

print("\n# Convert to list, tuple")
print(f"{list(tup)=}")
print(f"{tuple(tup)=}")

print("\n# Tuples are immutable, but we can make copy and add")
new_tup = OneBasedTuple(list(tup) + ["Dianna"])
print(f"{new_tup=}")
