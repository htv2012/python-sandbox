import dataclasses

import click

from clicklib import ArgsKwargs, ArgsKwargsParamType, ClassParamType


@dataclasses.dataclass
class Server:
    host: str
    port: int
    secured: bool


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    is_admin: bool


@click.command
@click.option("-d", "--data", type=ArgsKwargsParamType())
@click.option("-s", "--server", type=ClassParamType(Server))
@click.option("-u", "--user", type=ClassParamType(User))
def main(data: ArgsKwargs, server: Server, user: User):
    if server:
        print(f"{server=}")
    if data is not None:
        print(f"{data=}")
    if user:
        print(f"{user=}")


if __name__ == "__main__":
    main()
