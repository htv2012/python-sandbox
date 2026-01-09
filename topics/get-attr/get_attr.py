#!/usr/bin/env python3
"""
whatis: Get attribute of an object
"""

import contextlib
import io
import operator


def get_info(obj):
    buf = io.StringIO()
    buf.write(f"Object: {obj!r}")

    attr_list = [attr for attr in dir(obj) if not attr.startswith("__")]
    if attr_list:
        buf.write(" with attributes:\n")
    for attr in attr_list:
        buf.write(f"- {attr}\n")
    return buf.getvalue()


def get_attr(obj, *attrs, planb=True):
    """Entry"""
    getters = [operator.attrgetter(attr) for attr in attrs]
    if planb:
        getters.append(get_info)

    for getter in getters:
        with contextlib.suppress(AttributeError, TypeError):
            attr = getter(obj)
            if callable(attr):
                result = attr()
            else:
                result = attr
            return result

    raise ValueError(f"get_attr failed for {obj!r}")
