#!/usr/bin/env python
import functools
import itertools
import operator
import re


def _str2int(number_or_str):
    try:
        return int(number_or_str, 10)
    except ValueError:
        return number_or_str


def _make_equal_lengths(tuple1, tuple2):
    return itertools.zip_longest(tuple1, tuple2, fillvalue=0)


def parse_requirement(requirement_str: str):
    pattern = re.compile(
        r"""
        ^
        (>|>=|==) # The operator
        (((\d+|x)\.)*(\d+|x))    # digits or x
        $
        """,
        re.VERBOSE,
    )
    ops = {
        ">": operator.gt,
        ">=": operator.ge,
        "==": operator.eq,
    }

    normalized = requirement_str.strip().replace(" ", "").lower()
    matched = pattern.match(normalized)

    if not matched:
        raise ValueError(f"{requirement_str!r} is not in valid requirement format")

    op = ops[matched[1]]
    version_tuple = tuple(_str2int(n) for n in matched[2].split("."))
    return op, version_tuple


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
            if a != b:
                return False
        return True

    def __gt__(self, other):
        for num, other_num in _make_equal_lengths(
            self.version_tuple, other.version_tuple
        ):
            if other_num == "x" or num == other_num:
                continue
            if num > other_num:
                return True
            return False
        return False

    def satisfied(self, requirement: str):
        # TODO: Buggy
        op, requirement_tuple = parse_requirement(requirement)
        for num, required_num in zip(self.version_tuple, requirement_tuple):
            if required_num == "x":
                # wildcard matches anything
                continue
            if num == 3:
                breakpoint()
            if not op(num, required_num):
                return False
        return True
