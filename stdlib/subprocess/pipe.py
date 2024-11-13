#!/usr/bin/env python3
import shlex
import subprocess


def pipe_exec(command_chain):
    stdout = subprocess.PIPE
    stdin = subprocess.PIPE
    for command in command_chain:
        process = subprocess.Popen(
            command, stdin=stdin, stdout=stdout, encoding="utf-8"
        )
        stdin = process.stdout

    out, err = process.communicate()
    return out, err


def pipe_split(command_chain):
    commands = [shlex.split(cmd) for cmd in command_chain.split("|")]
    return commands


if __name__ == "__main__":
    # Command chain can be a string, like this
    command_chain = pipe_split("ls | fgrep .py | sed 's/^/- /'")
    print(command_chain)
    out, _ = pipe_exec(command_chain)
    print(out)

    # Or command chain can be a list of commands, like this
    command_chain = [("ls",), ("grep", "py"), ("sed", "s/^/- /")]
    print(command_chain)
    out, _ = pipe_exec(command_chain)
    print(out)
