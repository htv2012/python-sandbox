#!/usr/bin/env python

import settings

s = settings.Settings()
print(s)

try:
    print("---")
    s.shell = "bash"
    print("Name:", s.name)
    print("UID:", s.uid)
except AttributeError:
    pass

print("---")
for k, v in s.items():
    print("{}: {}".format(k, v))

s.save()
