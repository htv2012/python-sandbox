"""
Demo: Convert JSON string from command line arguments into objects
"""

import click

from clicklib import JsonParamType
from data import Server, Testbed, User


@click.command
@click.option("-s", "--server", type=JsonParamType(Server))
@click.option("-u", "--user", type=JsonParamType(User))
@click.option("-t", "--testbed", type=JsonParamType(Testbed))
def main(server: Server, user: User, testbed: Testbed):
    if server is not None:
        print(f"{server=}")
    if user is not None:
        print(f"{user=}")
    if testbed is not None:
        print(f"{testbed=}")


if __name__ == "__main__":
    main()
