#!/usr/bin/env python3
"""Demo: roundtrip a dict with int as keys."""

import json

original = {1: "Hello"}
json_text = json.dumps(original)
round_trip = json.loads(json_text)

print(f"{original=}")
print(f"{json_text=}")
print(f"{round_trip=}")
print("After round-trip conversion, the int key has been changed into str")
