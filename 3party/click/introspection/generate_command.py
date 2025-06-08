"""Generate command to run a click app."""

import argparse
import pathlib
import sys

import click


def query_param(param: click.Parameter):
    opts = sorted(param.opts)

    print()
    print("/".join(opts))
    if param.help:
        print(param.help)

    if param.is_flag and input("Include flag, y/n? ") == "y":
        return opts[0]
    elif param.type is click.BOOL and not param.is_flag:
        ans = input("true/false: ")
        if ans != "x":
            return f"{opts[0]} {ans}"
    elif isinstance(param.type, click.Choice):
        choices = [getattr(c, "name", c) for c in param.type.choices]
        print("Select a choice")
        print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
        ans = input("> ")
        if ans:
            return f"{opts[0]} {choices[int(ans)]}"
    else:
        ans = input("arg: ")
        if ans != "":
            return f"{opts[0]} {ans}"


def generate_args(cli):
    for param in cli.params:
        arg = query_param(param)
        if arg:
            yield arg

    sub_commands = getattr(cli, "commands", {})
    if not sub_commands:
        return

    choices = list(cli.commands)
    print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
    ans = input("> ")
    if not ans:
        return

    ans = choices[int(ans)]
    yield ans
    yield from generate_args(sub_commands[ans])


def generate_script(script, entry):
    cmd = [script.name]

    # Import
    sys.path.insert(0, str(script.parent))
    mod = __import__(script.stem)
    cli = getattr(mod, entry)
    del sys.path[0]

    cmd.extend(generate_args(cli))
    print()
    print(" \\\n".join(cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=pathlib.Path)
    parser.add_argument("entry")
    options = parser.parse_args()
    if not options.script.exists():
        raise SystemExit(f"{options.script} does not exist")
    generate_script(options.script, options.entry)


if __name__ == "__main__":
    main()
