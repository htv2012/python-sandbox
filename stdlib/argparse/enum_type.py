#!/usr/bin/env python
"""
Argparse and enum type
"""
import argparse
import enum


class Auth(enum.Enum):
    NONE = 0
    SIMPLE = 1
    SAML = 2

    @classmethod
    def from_str(cls, key):
        return cls[key.upper()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", default="NONE", type=Auth.from_str)

    options = parser.parse_args()
    print(options)


if __name__ == '__main__':
    main()
