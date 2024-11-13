#!/usr/bin/env python3
""" Uses NamedTuple to collect function's arguments """
import typing


class Arguments(typing.NamedTuple):
    """
    Class to gather all function's arguments. We can add alternate
    initialization, or custom methods here.
    """
    username: str
    password: str
    hostname: str
    port: int = 22


def login(username, password, hostname, port):
    concealed = "".join("*" for _ in password)
    print(f"Log in {username}@{hostname}:{port} with password {concealed}")


def main():
    opt = Arguments("user1", "i4got", "192.168.1.7")
    print(f"Arguments: {opt}")

    # Use as a function's arguments
    login(**opt._asdict())
    login(*opt)


if __name__ == '__main__':
    main()
