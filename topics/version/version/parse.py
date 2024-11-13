#!/usr/bin/env python3
"""
Parses package lines found in requirements.txt and "pip freeze"
"""


def parse_package(text):
    text = text.strip().replace(" ", "")
    operators = ["==", ">=", ">", "<=", "<"]

    for operator in operators:
        package, comparison, version = text.partition(operator)
        if comparison == operator and version != "":
            return package, comparison, version

    return text, "", ""


def filter_package(lines):
    for line in lines:
        if not line.strip():
            continue
        if line.lstrip()[0] in {'#', '-'}:
            continue
        yield line
