#!/usr/bin/env python3
"""Read the field blueprint from a text file."""
import csv
import dataclasses
import pydoc


def main():
    """Perform script."""
    with open("blueprint.csv") as stream:
        blueprint = [
            (field_name, pydoc.locate(field_type))
            for field_name, field_type in csv.reader(stream)
        ]

    User = dataclasses.make_dataclass("User", blueprint)

    with open("users.csv") as stream:
        for row in csv.reader(stream):
            user = User(*row)
            print(user)


if __name__ == "__main__":
    main()
