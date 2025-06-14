"""Generate command to run a click app."""

import argparse
import contextlib
import pathlib
import subprocess
import sys
from typing import List

import click


def menu(items: List) -> str:
    items = sorted(items)
    menu_text = "\n".join("%d. %s" % t for t in enumerate(items))
    subprocess.run(["column"], text=True, input=menu_text)

    while True:
        ans = input("Enter a number, or text: ")
        if ans == "" or ans in items:
            return ans
        with contextlib.suppress(ValueError, IndexError):
            return items[int(ans)]


def format_param(opt: str, value: str):
    if opt.startswith("--"):
        return f"{opt}={value}"
    elif opt.startswith("-"):
        return f"{opt}{value}"
    raise ValueError(f"Cannot handle {opt}, {value}")


def query_param(param: click.Parameter):
    opts = sorted(param.opts)

    print()
    if isinstance(param, click.Argument):
        breakpoint()
    # if isinstance(param, click.Argument):
    #     print()
    #     ans = input("arg: ")
    #     if
    print("/".join(opts))
    help_text = getattr(param, "help", param.__doc__)
    if help_text:
        print(help_text)

    if param.is_flag:
        ans = input("Include flag, y/n? ")
        if ans == "y":
            return opts[0]
    elif param.type is click.BOOL and not param.is_flag:
        ans = input("Bool flag, enter true or false: ")
        if ans != "":
            return f"{opts[0]} {ans}"
    elif isinstance(param.type, click.Choice):
        choices = [getattr(c, "name", c) for c in param.type.choices]
        # print("Select a choice")
        # print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
        # ans = input("> ")
        ans = menu(choices)
        if ans:
            # return f"{opts[0]} {ans}"
            return format_param(opts[0], ans)
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
    # print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
    # ans = input("> ")
    # if not ans:
    #     return

    # ans = choices[int(ans)]
    ans = menu(choices)
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
