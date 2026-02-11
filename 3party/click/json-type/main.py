"""
Demo: Convert JSON string from command line arguments into objects
"""

import click

from json_type.clicklib import EnumParamType, JsonParamType
from json_type.data import Server, Subject, Testbed, User


@click.command
@click.option("-j", "--subject", type=EnumParamType(Subject))
@click.option("-s", "--server", type=JsonParamType(Server))
@click.option("-u", "--user", type=JsonParamType(User))
@click.option("-t", "--testbed", type=JsonParamType(Testbed))
@click.option("-g", "--group", multiple=True, type=JsonParamType(Subject))
def main(group, subject: Subject, server: Server, user: User, testbed: Testbed):
    if group:
        print(f"{group=}")
    if subject is not None:
        print(f"{subject=}")
        print(f"  {subject.value=}")
        print(f"  {subject.weight=}")
    if server is not None:
        print(f"{server=}")
    if user is not None:
        print(f"{user=}")
    if testbed is not None:
        print(f"{testbed=}")


if __name__ == "__main__":
    main()
