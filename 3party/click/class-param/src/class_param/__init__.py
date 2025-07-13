import dataclasses
from typing import Optional

import click

from .clicklib import ClassParamType


@dataclasses.dataclass(frozen=True)
class User:
    uid: int
    alias: str
    is_admin: bool
    shell: Optional[str] = "bash"

    param_type = dict(uid=int, alias=str, is_admin=bool, shell=str)


class Server:
    param_type = dict(host=str, port=int)

    def __init__(self, host, port=None):
        self.host = host
        self.port = port or 2200

    def __repr__(self):
        return f"Server(host={self.host!r}, port={self.port!r})"


@click.command
@click.option("-u", "--user", type=ClassParamType(User))
@click.option("-s", "--server", type=ClassParamType(Server))
def main(user, server) -> None:
    if user is not None:
        print(f"{user=}")
    if server is not None:
        print(f"{server=}")
