#!/usr/bin/env python3
"""
Parses the shell commands, including redirections
"""

import io
import shlex


def parse_cmd(cmd):
    buf = io.StringIO(cmd)
    lex = shlex.shlex(buf, punctuation_chars=True)

    cmds = []
    subcmd = []

    for token in lex:
        if token == "|":
            cmds.append(subcmd)
            subcmd = []
        elif token == ">" or token == ">>":
            out_file = next(lex)
            if subcmd:
                cmds.append(subcmd)
                subcmd = []
            cmds.append([token, out_file])
        else:
            subcmd.append(token)
    if subcmd:
        cmds.append(subcmd)
    return cmds


def main():
    """Entry"""
    while True:
        cmd = input("parse> ")
        if cmd == "q":
            break
        for subcmd in parse_cmd(cmd):
            print(subcmd)
        print()


if __name__ == "__main__":
    main()
