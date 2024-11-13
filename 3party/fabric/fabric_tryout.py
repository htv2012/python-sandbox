#!/usr/bin/env python3
import argparse

import fabric


def run_demo(connection: fabric.Connection):
    print("\n# Run a command and do not hide output")
    result = connection.run("pwd")
    # stdout and stderr are always captured and stored in the Result
    # object, regardless of hide’s value.
    assert result.stdout is not None

    print("\n# Run a command and hide the output")
    result = connection.run("cat /etc/os-release", hide=True)
    print(result.stdout)


def show_result_details(connection: fabric.Connection):
    print("\n# About the Result object")
    print("# Note that stdout and stderr are strings, not bytes")
    result = connection.run("pwd", hide=True)
    for name, value in sorted(vars(result).items()):
        print(f"- {name} = {value!r}")


def cd_demo(connection: fabric.Connection):
    print("\n# Run a command inside a directory")
    with connection.cd("/usr/bin"):
        connection.run("pwd")


def download_demo(connection: fabric.Connection):
    print("\n# Download /etc/os-release")
    local_path = "/tmp/os-release"
    connection.get("/etc/os-release", local_path)
    with open(local_path, mode="r", encoding="utf-8") as stream:
        print(stream.read())


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    options = parser.parse_args()

    connection = fabric.Connection(host=options.host)
    run_demo(connection)
    show_result_details(connection)
    cd_demo(connection)
    download_demo(connection)


if __name__ == "__main__":
    main()
