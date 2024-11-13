#!/usr/bin/env python3
"""Demo a read-only dictionary."""
from types import MappingProxyType

# mydict is a real dictionary, rodict is a proxy, a read-only dict
mydict = dict(a=1, b=2, c=3)
rodict = MappingProxyType(mydict)

# It acts like a real dictionary
for key, value in rodict.items():
    print(f"{key} = {value}")

# However, we cannot modify it
try:
    rodict["c"] = 30
except TypeError as error:
    print("Cannot modify the proxy")
    print(error)
