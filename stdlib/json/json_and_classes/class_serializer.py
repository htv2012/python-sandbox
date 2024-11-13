"""Provide a way to serialize classes."""

import functools


@functools.singledispatch
def serialize_object(obj):
    obj_type = obj.__class__.__name__
    raise TypeError(f"Object of type {obj_type} is not JSON serializable")
