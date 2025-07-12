import dataclasses
import typing

import click


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: typing.Optional[str] = "zsh"
    serial: int = dataclasses.field(default=101)


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


class DataclassParamType2(click.ParamType):
    """A different approach."""

    def __init__(self, cls, cast):
        self.cls = cls
        self._cast = cast

    def cast(self, key, value, param, ctx):
        try:
            type_ = self._cast[key]
            return type_(value)
        except ValueError:
            self.fail(f"Invalid argument: {value}", param, ctx)

    def convert(self, value, param, ctx):
        kwargs = dict(kv.split("=") for kv in value.split(","))
        kwargs = {k: self.cast(k, v, param, ctx) for k, v in kwargs.items()}
        print(f"{kwargs=}")
        ret = self.cls(**kwargs)
        print(f"{ret=}")
        return ret


@click.command
@click.option(
    "--admin",
    type=DataclassParamType2(
        User, {"uid": int, "alias": str, "shell": str, "serial": int}
    ),
)
@click.argument("user", type=DataclassParamType(User))
def main(user, admin) -> None:
    print(f"{user=}")
    print(f"{admin=}")
