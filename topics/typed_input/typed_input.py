#!/usr/bin/env python3
"""
This module provides a convenient function `typed_input` which behaves like
`input`, but returns an object of a type other than str.
"""


def typed_input(prompt, return_type=str, input_proc=input, retries=1):
    """
    This function behaves like input(), but return a caller-specified type

    :param prompt: The prompt, same as in input()
    :param return_type: The return type such as str, int, float, ...
    :param retries: Number of retries
    :return: the value which has been casted
    """
    for _ in range(retries):
        try:
            raw_value = input_proc(prompt)
            typed_value = return_type(raw_value)
            return typed_value
        except ValueError:
            print("Invalid value: {!r}, try again".format(raw_value))

    raise ValueError(
        "Invalid input {!r} for type {!r}".format(raw_value, return_type.__name__)
    )


def float_input(prompt, input_proc=input, retries=1):
    """
    This function behaves like input(), but returns a float.
    See typed_input() for parameters.
    """
    return typed_input(
        prompt, return_type=float, input_proc=input_proc, retries=retries
    )


def int_input(prompt, input_proc=input, retries=1):
    """
    This function behaves like input(), but returns an int.
    See typed_input() for parameters.
    """
    return typed_input(prompt, return_type=int, input_proc=input_proc, retries=retries)
