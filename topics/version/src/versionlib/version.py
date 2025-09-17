#!/usr/bin/env python
import functools
import itertools
import operator
import re


def _str2int(text: str):
    try:
        return int(text, 10)
    except ValueError:
        return text.lower()


def _make_equal_lengths(tuple1, tuple2):
    return itertools.zip_longest(tuple1, tuple2, fillvalue=0)


def parse_requirement(requirement_str: str):
    pattern = re.compile(
        r"""
        ^
        (>|>=|==)?       # The operator, optional
        (
            ((\d+|x)\.)*  # digits or x, followed by dot 0-n times
            (\d+|x)       # digits or x
        )
        $
        """,
        re.VERBOSE,
    )
    ops = {
        None: operator.eq,
        ">": operator.gt,
        ">=": operator.ge,
        "==": operator.eq,
    }

    normalized = requirement_str.strip().replace(" ", "").lower()
    matched = pattern.match(normalized)

    if not matched:
        raise ValueError(f"{requirement_str!r} is not in valid requirement format")

    op = ops[matched[1]]
    required_version = Version(matched[2])
    return op, required_version


@functools.total_ordering
class Version:
    def __init__(self, version_str):
        self.version_str = version_str.strip()
        self.version_tuple = tuple(_str2int(n) for n in self.version_str.split("."))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.version_str!r})"

    def __str__(self):
        return self.version_str

    def __eq__(self, other):
        for a, b in _make_equal_lengths(self.version_tuple, other.version_tuple):
            if b == "x":
                continue
            if a != b:
                return False
        return True

    def __gt__(self, other):
        for num, other_num in _make_equal_lengths(
            self.version_tuple, other.version_tuple
        ):
            if other_num == "x" or other_num == num:
                continue
            if num > other_num:
                return True
            return False
        return False

    def satisfied(self, requirement: str):
        op, required_version = parse_requirement(requirement)
        return op(self, required_version)
