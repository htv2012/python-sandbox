import dataclasses
import datetime
import enum
import pathlib
from types import SimpleNamespace
from typing import Optional

import click


class RunType(str, enum.Enum):
    MANUAL = "manual"
    NIGHTLY = "nightly"


@dataclasses.dataclass(frozen=True)
class SshServer:
    host: str
    port: int = 22

    def __post_init__(self):
        assert isinstance(self.port, int)
        assert self.host is not None
        assert self.host != ""

    @classmethod
    def from_str(cls, value: str):
        tokens = value.split(":")
        if len(tokens) == 2:
            tokens[1] = int(tokens[1])
        return cls(*tokens)


@dataclasses.dataclass()
class Car:
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None


class CarParam(click.ParamType):
    name = "Car"

    def convert(self, value, param, ctx):
        flags = "/".join(param.opts)
        tokens = [token or None for token in value.split(",")]

        if tokens[0] is not None:
            try:
                tokens[0] = int(tokens[0])
            except ValueError:
                ctx.fail(f"For {flags}, year must be an integer")

        if len(tokens) != 3:
            ctx.fail(f"For {flags}, expect argument to be year,make,model")
        return Car(*tokens)


@click.group
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.option("-c", "--confirm", type=click.BOOL)
@click.option("-d", "--date", type=click.DateTime(), default=datetime.datetime.today())
@click.option(
    "-D",
    "--root-dir",
    type=click.Path(
        dir_okay=True,
        exists=True,
        file_okay=False,
        path_type=pathlib.Path,
        resolve_path=True,
        writable=True,
    ),
    default=pathlib.Path(".").resolve(),
)
@click.option("-r", "--run-type", type=click.Choice(RunType, case_sensitive=False))
@click.option("-s", "--server", type=SshServer.from_str)
@click.option("-t", "--transport", type=CarParam())
@click.pass_context
def main(ctx, verbose):
    """Entry point"""
    ctx.ensure_object(SimpleNamespace)
    ctx.obj.verbose = verbose


@main.command
@click.pass_context
def foo(ctx):
    print("# foo")
    print(f"verbose: {ctx.obj.verbose}")


@main.command
@click.pass_context
def bar(ctx):
    print("# bar")
    print(f"verbose: {ctx.obj.verbose}")


if __name__ == "__main__":
    main()
