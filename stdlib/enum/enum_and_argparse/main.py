#!/usr/bin/env python3
"""
Use enum with argparse
"""
import argparse
import enum

class Transport(enum.StrEnum):
    HTTPS = "https"
    SSH = "ssh"

    @classmethod
    def _missing_(cls, value: str):
        """Case-insensitive lookup value"""
        return cls(value.lower())


parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--transport",
    type=Transport,
    default="https",
    choices=[t.value for t in Transport],
)
options = parser.parse_args()
print(options)

