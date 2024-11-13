#!/usr/bin/env python
"""
Sample to show parsing of key-value text
"""
import pathlib

from hvtext import kv


BLOCK = """
name = John Doe
alias = johnd
user_id = 501
shell = bash
""".splitlines()


SCRIPT_DIR = pathlib.Path(__file__).parent
WITH_EQUAL = SCRIPT_DIR / 'kv_with_equal.txt'
WITH_COLON = SCRIPT_DIR / 'kv_with_colon.txt'


def main():
    """ Entry point """
    # File with equal sign as separator
    print('\nParse file with equual sign:')
    with open(WITH_EQUAL) as file_handle:
        parsed_dict = kv.parse(file_handle)
        print(parsed_dict)

    print('\nParse file with colon:')
    # File with colon as a separator
    with open(WITH_COLON) as file_handle:
        parsed_dict = kv.parse(file_handle, separator=':')
        print(parsed_dict)

    print('\nParse from block of text:')
    parsed_dict = kv.parse(BLOCK)
    print(parsed_dict)

    print('\nParse from a single line of text')
    text = "name: John Doe; alias: johnd; user_id: 501; shell: bash"
    parsed_dict = kv.parse(text.split(';'), separator=':')
    print(parsed_dict)



if __name__ == '__main__':
    main()

