import dataclasses
import typing

import click


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: typing.Optional[str] = "zsh"


class DataclassParamType(click.ParamType):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def cast(self, key, value, param, ctx):
        for field in dataclasses.fields(self.cls):
            if field.name == key:
                return field.type(value)
        self.fail(f"Invalid field {key!r} for {self.cls.__name__}", param, ctx)

    def convert(self, value, param, ctx):
        args = value.split(",")
        if "=" in value:
            kwargs = {
                k: self.cast(k, v, param, ctx)
                for k, v in dict(arg.split("=") for arg in args).items()
            }
            return self.cls(**kwargs)


@click.command
@click.argument("user", type=DataclassParamType(User))
def main(user) -> None:
    print(f"{user=}")
