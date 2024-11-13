#!/usr/bin/env python3
"""
Parse variables from a bash scripts. Those that starts with "export"
"""
import shlex


def main():
    """ Entry """
    vars_dict = {}
    with open("myscript.sh") as stream:
        lex = shlex.shlex(stream)

        # Tells shlex to process the "source" command
        lex.source = "source"

        for token in lex:
            if token == "export":
                # Parses "export key=value"
                key = next(lex)
                next(lex)  # equal sign
                value = next(lex)
                vars_dict[key] = value

    print(vars_dict)

if __name__ == "__main__":
    main()

