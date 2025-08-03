#!/usr/bin/env python3
"""
A Python skeleton script
"""

import itertools


def peek(obj, default=None):
    scratch, original = itertools.tee(obj)
    return next(scratch, default), original
