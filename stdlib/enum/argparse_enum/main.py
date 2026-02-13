#!/usr/bin/env python3
"""
Use enum with argparse
"""

import argparse
import enum


class Transport(enum.StrEnum):
    HTTP = "http"
    HTTPS = "https"
    SSH = "ssh"

    @classmethod
    def from_str(cls, value: str):
        return cls(value.lower())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", type=Transport.from_str, default="https", choices=Transport
    )
    options = parser.parse_args()
    print(f"Transport: {options.t!r}")
    print()


if __name__ == "__main__":
    main()
