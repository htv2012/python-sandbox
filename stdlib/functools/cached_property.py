"""Differences between cached property and cached_property"""

import functools


class Foo:
    @property
    @functools.lru_cache
    def bar(self):
        print("Calculating bar")
        return "bar value"

    @functools.cached_property
    def baz(self):
        print("Calculating baz")
        return "baz value"


print("\n")
print("#")
print("# cached_property.py")
print("#")
foo = Foo()

print("\n# First access")
v1 = foo.bar
v2 = foo.baz
print(f"foo.bar={v1!r}")
print(f"foo.baz={v2!r}")

print("\n# Second access")
v1 = foo.bar
v2 = foo.baz
print(f"foo.bar={v1!r}")
print(f"foo.baz={v2!r}")

print("\n# Cached property is read-only")
try:
    foo.bar = "new bar"
except AttributeError as error:
    print(f"Setting foo.bar generates an exception: {error}")

print("\n# cached_property is not")
foo.baz = "new baz"
print(f"{foo.baz=}")

print("\n# Reset cached_property by deleting the baz attribute")
delattr(foo, "baz")
print(f"{foo.baz=}")
