from typing import Optional

import click

__all__ = ["ClassParamType"]


class ClassParamType(click.ParamType):
    def __init__(self, cls, cast: Optional[dict] = None):
        super().__init__()
        self.cls = cls
        cast = cast or getattr(cls, "param_type", None)
        if cast is None:
            raise ValueError("Please supply a cast")
        self.kwargs_cast = cast
        self.args_cast = tuple(cast.values())

    def add_arg(self, index, value, args, param, ctx):
        try:
            cast = self.args_cast[index]
            args.append(cast(value))
        except ValueError:
            self.fail(
                f"Expect {value!r} to be of type {cast.__name__} ", param=param, ctx=ctx
            )

    def add_kwarg(self, key, value, kwargs, param, ctx):
        try:
            cast = self.kwargs_cast[key]
            kwargs[key] = cast(value)
        except ValueError:
            self.fail(
                f"For {key}={value}. Expected {value!r} to be of type {cast.__name__}",
                param=param,
                ctx=ctx,
            )
        except KeyError:
            self.fail(f"{key!r} is not a valid keyword argument", param=param, ctx=ctx)

    def convert(self, value, param, ctx):
        tokens = value.split(",")
        args = []
        kwargs = {}

        for index, token in enumerate(tokens):
            kv = token.split("=")
            if len(kv) == 2:
                self.add_kwarg(*kv, kwargs, param, ctx)
            elif len(kv) == 1:
                self.add_arg(index, token, args, param, ctx)
            else:
                self.fail(f"Invalid arg: {token}", param, ctx)
        try:
            return self.cls(*args, **kwargs)
        except ValueError as error:
            self.fail(f"Invalid argument: {value}, reason: {error}")
