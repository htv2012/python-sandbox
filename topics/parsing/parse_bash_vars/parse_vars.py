#!/usr/bin/env python3
"""
Parse variables from a bash scripts. Those that starts with "export"
"""

import pprint
import shlex
import string


def substitute(di: dict):
    di_copy = {k: string.Template(v).safe_substitute(**di) for k, v in di.items()}
    return di_copy


def main():
    """Entry"""
    vars_dict = {}
    with open("myscript.sh") as stream:
        lex = shlex.shlex(stream, posix=True)

        # Tells shlex to process the "source" command
        lex.source = "source"

        for token in lex:
            if token == "export":
                # Parses "export key=value"
                key = next(lex)
                next(lex)  # equal sign
                value = next(lex)
                vars_dict[key] = value

    new_dict = substitute(vars_dict)
    pprint.pprint(new_dict)


if __name__ == "__main__":
    main()
