#!/usr/bin/env python3
""" Explores the CSV dialects """
import csv


if __name__ == "__main__":
    # Register a custom dialect to see how it comes out
    csv.register_dialect(
        "my custom",
        lineterminator="\n",
        skipinitialspace=True,
    )

    # List all the dialects and their properties
    for dialect_name in csv.list_dialects():
        print(f"Dialect: {dialect_name}")

        dialect = csv.get_dialect(dialect_name)
        print(f"- delimiter: {dialect.delimiter!r}")
        print(f"- doublequote: {dialect.doublequote!r}")
        print(f"- escapechar: {dialect.escapechar!r}")
        print(f"- lineterminator: {dialect.lineterminator!r}")
        print(f"- quotechar: {dialect.quotechar!r}")
        print(f"- quoting: {dialect.quoting!r}")
        print(f"- skipnitialspace: {dialect.skipinitialspace!r}")
        print(f"- strict: {dialect.strict!r}")
