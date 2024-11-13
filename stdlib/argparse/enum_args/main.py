"""Exercise the enum_choice_action."""

import argparse
import enum

from argparse_enum import enum_choice_action


class Connection(enum.IntEnum):
    insecured = 80
    secured = 8443


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--connection",
        action=enum_choice_action(Connection),
        default=Connection.secured,
    )
    options = parser.parse_args()
    # print(f"{options=}")
    connection = options.connection
    print(f"Making a {connection.name} connection using port {connection.value}")


if __name__ == "__main__":
    main()
