#!/usr/bin/env python3
import os
import pathlib
import shlex
import subprocess


def get_shell_info():
    shell = os.getenv("SHELL")
    assert shell is not None
    stem = pathlib.Path(shell).stem

    home = os.getenv("HOME")
    assert home is not None
    startup = f"{home}/.{stem}rc"

    return shell, startup


def get_shell_aliases(shell_path, shell_startup):
    command = [
        shell_path,
        "-c",
        f"source '{shell_startup}'; alias",
    ]
    completed_process = subprocess.run(
        command,
        text=True,
        capture_output=True,
    )

    aliases = dict(
        [token.strip("'") for token in line.split("=", 1)]
        for line in completed_process.stdout.splitlines()
    )
    return aliases


def lookup_command(command, aliases: dict = None):
    aliases = aliases or {}
    output = []
    while (expanded := aliases.get(command, command)) != command:
        output = shlex.split(expanded) + output
        if output[0] == command:
            # recursive alias: alias grep="grep ..."
            return output
        command = output.pop(0)
    output.insert(0, command)
    return output


def main():
    """Entry"""
    path, rc = get_shell_info()
    aliases = get_shell_aliases(path, rc)
    for command in ["cd", "ls", "ll", "find", "grep"]:
        print(f"\n# {command}")
        output = lookup_command(command, aliases)
        print(output)


if __name__ == "__main__":
    main()
