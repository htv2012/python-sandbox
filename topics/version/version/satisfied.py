#!/usr/bin/env python3
import logging
import operator
import os

from .version import Version


logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger(__name__)


def satisfied(actual, comparison, requirement):
    """
    Returns True if the `actual` version satisfied the requirement
    """
    # No version requirement means any version will do
    if comparison == "" and requirement == "":
        return True

    compare_operator = {
        "==": operator.eq,
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
    }

    actual = Version(actual)
    requirement = Version(requirement)
    return compare_operator[comparison](actual, requirement)