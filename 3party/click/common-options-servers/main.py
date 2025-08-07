import dataclasses
import functools

import click


@dataclasses.dataclass(frozen=True)
class Server:
    host: str
    port: int

    def __str__(self):
        return f"{self.host}:{self.port}"


def server(fn):
    @click.option("--host", default="localhost")
    @click.option("--port", default=2200, type=int)
    @click.pass_context
    @functools.wraps(fn)
    def inner(ctx, *args, **kwargs):
        ctx.ensure_object(dict)
        host = kwargs.pop("host")
        port = kwargs.pop("port")
        ctx.obj["server"] = Server(host, port)
        return fn(*args, **kwargs)

    return inner


@click.group()
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)


@main.command
@server
@click.pass_obj
def connect(obj):
    print(f"connect to {obj['server']}")


@main.command
@server
@click.pass_obj
def disconnect(obj):
    print(f"disconnect from {obj['server']}")


if __name__ == "__main__":
    main()
