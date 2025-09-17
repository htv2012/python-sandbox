from versionlib import Version

v = Version("1.5.3")
# s = v.satisfied(">1.5.2")
r = Version("1.5.X")
assert v == r
