import dataclasses
import json

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

    @classmethod
    def from_str(cls, text: str):
        kwargs = dict(kv.split("=") for kv in text.split(","))
        kwargs["uid"] = int(kwargs["uid"])
        kwargs["is_admin"] = bool(kwargs["is_admin"])
        return cls(**kwargs)


@click.command
@click.option("-d", "--data", type=ArgsKwargsParamType())
@click.option("-s", "--server", type=ClassParamType(Server))
@click.option("-u", "--user", type=ClassParamType(User), metavar="uid,alias,is_admin")
@click.option("--user2", type=User.from_str)
@click.option("--raw", type=json.loads, help="Raw JSON", default="{}")
def main(data: ArgsKwargs, server: Server, user: User, user2: User, raw):
    if server:
        print(f"{server=}")
    if data is not None:
        print(f"{data=}")
    if user:
        print(f"{user=}")
    if user2:
        print(f"{user2=}")
    print(f"raw={json.dumps(raw, indent=4)}")


if __name__ == "__main__":
    main()
