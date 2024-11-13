#!/usr/bin/env python3
from requirements import Requirements


req = Requirements()
with open("sample-requirements.txt") as stream:
    req.parse(stream.read())

print("Flags:")
for flag in req.flags:
    print(flag)

print("=" * 80)
print("Dependencies:")
for dep in sorted(req):
    print(dep)