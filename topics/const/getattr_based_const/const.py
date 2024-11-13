#!/usr/bin/env python3


class Const:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        attrs = ", ".join("%s=%r" % kv for kv in self.__dict__.items())
        return f"Const({attrs})"

    def __iter__(self):
        return iter(self.__dict__.values())

    def __setattr__(self, key, value):
        if key != "__dict__":
            raise TypeError("This object is read-only")
        super().__setattr__(key, value)
