#!/usr/bin/env python3
"""
A CLI interface into pinboard
"""
import argparse
import collections.abc
import inspect


def parse_command_line():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='mycmd', required=True)

    sub_parsers.add_parser('notes')
    sub_parsers.add_parser('ls')
    sub_parsers.add_parser('export')

    argument_parser = sub_parsers.add_parser('new')
    argument_parser.add_argument('-t', '--tags')
    argument_parser.add_argument(
        '-s', '--shared',
        default='no',
        action='store_const',
        const='yes')
    argument_parser.add_argument(
        '-r', '--toread',
        default='no',
        action='store_const',
        const='yes')
    argument_parser.add_argument('url')
    argument_parser.add_argument('description')

    argument_parser = sub_parsers.add_parser('rm')
    argument_parser.add_argument('urls', nargs='+')

    return parser


def explore(obj, heading):
    print('-' * 80)
    print(heading)
    print('-' * 80)

    print(f'- Type: {type(obj)}')

    print('- Attributes')
    methods = {}
    for name in dir(obj):
        if name.startswith('__'):
            continue
        value = getattr(obj, name)
        if callable(value):
            methods[name] = value
        else:
            if (
                    isinstance(value, collections.abc.Sequence)
                    and not isinstance(value, str)
            ):
                print(f'   - {name}:')
                for element in value:
                    print(f'      - {element}')
            elif isinstance(value, collections.abc.Mapping):
                print(f'   - {name}: {type(value).__qualname__}')
                for key, value in value.items():
                    print(f'      - {key}: {value!r}')
            else:
                print(f'   - {name}: {type(value).__qualname__} = {value!r}')

    print('- Methods')
    for name, method in methods.items():
        signature = inspect.signature(method)
        print(f'   - {name}{signature}')


def main():
    """
    Entry
    """
    parser = parse_command_line()
    explore(parser, 'Parser')
    for index, action in enumerate(parser._actions):
        explore(action, f'parser._actions[{index}]')
        if action.choices:
            for choice_name, choice in action.choices.items():
                explore(
                    choice,
                    f'parser._actions[{index}].choices[{choice_name!r}]'
                )


if __name__ == '__main__':
    main()
