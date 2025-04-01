#!/usr/bin/env python
"""
Create constants that cannot be altered
"""

import collections


def define(_name=None, **names_values):
    """
    Defines a set of constants. Example usage:

        COLOR = define(RED='0xff0000', GREEN='0x00ff00', BLUE='0x0000ff')
        background = COLOR.BLUE
        print(background)  # output: 0x0000ff

    :param names_values: pairs of names and values for each constants
    :return: A set of constants, see example usage above
    """
    blue_print = collections.namedtuple(_name or "const", names_values)
    const = blue_print(**names_values)
    return const


def add(old_const, **names_values):
    """
    Adds more constants into a set and returns a new set with constants
    from the previous set combined with the new ones. Any attempt to
    redefine the existing constants will result in ValueError being
    thrown.

    :param old_const: The existing constants, created by define
    :param names_values: pairs of names and values for each constants
    :return: A new set of constants
    """
    # Ensure no duplication of names, that means we do not allow redefining a
    # constant
    old_names = set(old_const._asdict().keys())
    duplicates = old_names.intersection(names_values.keys())
    if duplicates:
        duplicates = ", ".join(duplicates)
        raise ValueError(f"Duplicate names: {duplicates} not allowed")

    # Create a new constant set with old and new names/values
    new_names_values = dict(**old_const._asdict(), **names_values)
    return define(**new_names_values)
