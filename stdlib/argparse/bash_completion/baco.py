#!/usr/bin/env python3
"""
Bash completion generator for python scripts which use argparse
"""
import argparse
import io
import json
import logging
import os
import re
import subprocess


logging.basicConfig(level=os.getenv('LOGLEVEL', 'WARN'))
LOGGER = logging.getLogger(__name__)


def get_help(cmd):
    output = subprocess.check_output(
        cmd + ['-h'],
        encoding='utf-8',
    )
    return output


def parse_optionals(lines):
    pattern = re.compile(r'-{1,2}\S+')
    optionals = []
    for line in lines:
        if line == '':
            break

        matched = pattern.findall(line)
        optionals.extend(matched)
    return optionals


def parse_positionals(app, lines):
    LOGGER.debug(f'lines={lines}')
    opts = []
    for line in lines:
        LOGGER.debug(f'line={line!r}')
        line = line.strip()
        if line == '':
            break
        if '{' in line:
            sub_commands = line[1:-1].split(',')
            sub_help = {}
            for sub_command in sub_commands:
                LOGGER.debug(f'sub_command={sub_command}')
                command = app + [sub_command]
                LOGGER.debug(f'command={command}')
                sub_help[sub_command] = parse_help(command)
            opts.append(sub_help)
        else:
            opts.append(line)

    return opts


def parse_help(app):
    """
    Parses the help text and return a set of positional and optional
    arguments
    """
    help_text = get_help(app)
    lines = help_text.splitlines()
    # TODO: Remove block
    for n, line in enumerate(lines):
        print(f'{n:>3}: {line}')

    optionals = []
    try:
        optional_index = lines.index('optional arguments:') + 1
        optionals = parse_optionals(lines[optional_index:])
    except ValueError:
        pass

    positionals = []
    try:
        positional_index = lines.index('positional arguments:') + 1
        positionals = parse_positionals(app, lines[positional_index:])
        print(f'Positionals={positionals}')
    except ValueError:
        pass

    return dict(optionals=optionals, positionals=positionals)


def generate_bash_completion(args):
    buf = io.StringIO()
    json.dump(args, buf, sort_keys=True, indent=4)
    print(buf.getvalue())

def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument('app', nargs='+')
    options = parser.parse_args()

    args = parse_help(options.app)
    generate_bash_completion(args)


if __name__ == '__main__':
    main()
