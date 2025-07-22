import dataclasses
from typing import Optional

import click

from .clicklib import ClassParamType


@dataclasses.dataclass(frozen=True)
class User:
    """A user."""

    uid: int
    alias: str
    is_admin: bool
    shell: Optional[str] = "bash"

    param_type = dict(uid=int, alias=str, is_admin=bool, shell=str)


class Server:
    """Non-dataclass."""

    param_type = dict(host=str, port=int)

    def __init__(self, host, port=None):
        self.host = host
        self.port = port or 2200

    def __repr__(self):
        return f"Server(host={self.host!r}, port={self.port!r})"

    @classmethod
    def from_str(cls, value: str):
        """Create an instant from a string value.

        Example:
            Server.from_str("myhost.com,2233")
        """
        tokens = value.split(",")
        count = len(tokens)

        if count == 1:
            return cls(tokens[0])
        elif count == 2:
            tokens[1] = int(tokens[1])
            return cls(*tokens)

        raise ValueError(f"Expect 1 or 2 arguments, got {count}: {value}")


@click.command
@click.option(
    "-u",
    "--user",
    metavar="UID,ALIAS,IS_ADMIN,SHELL",
    type=ClassParamType(User),
    help=(
        "\b\n"
        "A user, which consists of:\n"
        "- uid: int\n"
        "- alias: str\n"
        "- is_admin: bool\n"
        "- shell: str = bash\n\n"
        "\b\n"
        "Examples:\n"
        "  --user 501,anna,true\n"
        "  --user uid=501,is_admin=true,alias=anna,shell=bash"
    ),
)
@click.option("-s", "--server", metavar="HOST,PORT", type=ClassParamType(Server))
def main(user, server) -> None:
    if user is not None:
        print(f"{user=}")
    if server is not None:
        print(f"{server=}")
