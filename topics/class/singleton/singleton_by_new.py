#!/usr/bin/env python3
"""
Create a singleton using __new__

Pros:
- Fairly simple

Cons:
- Has to do this for every classes, or
- Has to do this via inheritance
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            print("x")
            cls._instance = object.__new__(cls, *args, **kwargs)
            print("y")
            # cls._instance.__init__(*args, **kwargs)
            print("z")
        return cls._instance

    def __init__(self, name):
        print(f"init({name})")
        self.name = name


if __name__ == "__main__":
    print(1)
    s1 = Singleton("foo")
    print(f"s1.name={s1.name}")
    s2 = Singleton("bar")
    print(f"s2.name={s2.name}")
    print(3)
    assert s1 is s2
    assert s2.name == "foo"
