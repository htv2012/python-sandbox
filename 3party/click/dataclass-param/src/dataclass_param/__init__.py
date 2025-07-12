import dataclasses
import typing
from typing import Dict, Optional

import click


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: typing.Optional[str] = "zsh"
    serial: int = dataclasses.field(default=101)

    # Instruction on how to cast str to an attribute
    cast = {"uid": int, "serial": int}


class DataclassParamType(click.ParamType):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def cast(self, key, value, param, ctx):
        for field in dataclasses.fields(self.cls):
            if field.name != key:
                continue
            if getattr(field.type, "_name", None) == "Optional":
                type_ = field.type.__args__[0]
            else:
                type_ = field.type
            return type_(value)
        self.fail(f"Invalid field {key!r} for {self.cls.__name__}", param, ctx)

    def convert(self, value, param, ctx):
        args = value.split(",")
        if "=" in value:
            kwargs = {
                k: self.cast(k, v, param, ctx)
                for k, v in dict(arg.split("=") for arg in args).items()
            }
            return self.cls(**kwargs)


class ClassParamType(click.ParamType):
    """Generic classes."""

    def __init__(self, cls=None, cast: Optional[Dict[str, str]] = None):
        self.cls = cls
        self._cast = cast or {}

    def cast(self, key, value, param, ctx):
        try:
            type_ = self._cast[key]
            return type_(value)
        except ValueError:
            self.fail(f"Invalid argument: {value}", param, ctx)
        except KeyError:
            # There is no instruction to cast, return value as is
            return value

    def convert(self, value, param, ctx):
        kwargs = dict(kv.split("=") for kv in value.split(","))
        kwargs = {k: self.cast(k, v, param, ctx) for k, v in kwargs.items()}
        if self.cls is not None:
            return self.cls(**kwargs)
        return kwargs


@click.command
@click.option("--admin", type=ClassParamType(User, User.cast))
@click.option("--user", type=DataclassParamType(User))
@click.option("--raw", type=ClassParamType(cast={"foo": int, "bar": float}))
def main(user, admin, raw) -> None:
    print(f"{user=}")
    print(f"{admin=}")
    print(f"{raw=}")
