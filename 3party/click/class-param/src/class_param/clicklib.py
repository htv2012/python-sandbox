import contextlib
import json

import click

__all__ = ["ClassParamType"]


def jsonify(value):
    with contextlib.suppress(json.JSONDecodeError):
        value = json.loads(value)
    return value


class ClassParamType(click.ParamType):
    """A click ParamType which converts an argument to a class object."""

    name = "csv-args"

    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def convert(self, value, param, ctx):
        with contextlib.suppress(AttributeError, TypeError, ValueError):
            return self.cls.from_str(value)

        tokens = value.split(",")
        args = []
        kwargs = {}

        for token in tokens:
            kv = token.split("=")
            if len(kv) == 2:
                key, value_ = kv
                kwargs[key] = jsonify(value_)
            elif len(kv) == 1:
                args.append(jsonify(token))
            else:
                self.fail(f"Invalid arg: {token}", param, ctx)

        try:
            return self.cls(*args, **kwargs)
        except ValueError as error:
            self.fail(f"Invalid argument: {value}, reason: {error}")
