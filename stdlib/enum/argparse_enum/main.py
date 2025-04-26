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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=Transport, default="https", choices=Transport)
    options = parser.parse_args()
    print(f"Transport: {options.t!r}")


if __name__ == "__main__":
    main()
