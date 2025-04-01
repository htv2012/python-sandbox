#!/usr/bin/env python
"""
Data Validators
Source: https://www.youtube.com/watch?v=S_ipdVNSFlo&ab_channel=%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9%D0%90%D0%B9%D1%82%D0%B8%D0%BF%D0%B8%D0%BF%D0%BB%D0%BE%D0%B2
at 36:22
"""

import abc


class Validator(abc.ABC):
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abc.abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):
    def __init__(self, *allowed):
        self.allowed = allowed

    def validate(self, value):
        if value not in self.allowed:
            raise ValueError(
                f"Expect value to be in {self.allowed}, but got {value!r}."
            )


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Expect {value!r} be an int or float")

        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f"Expect value not less than {self.minvalue}, but got {value!r}."
            )

        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f"Expect value not greater than {self.maxvalue}, but got {value!r}."
            )


if __name__ == "__main__":

    class Speaker:
        topic = OneOf("python", "computing")
        sid = Number(minvalue=1001, maxvalue=1999)

    speaker = Speaker()
