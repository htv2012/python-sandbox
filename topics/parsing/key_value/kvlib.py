"""
Parses key-values block of text
"""

import csv
import fileinput
import io
import json


def parse(text_or_file_object) -> dict:
    """
    Given a block of multiline text or a file-like object which represents
    lines of key/value, attempt to parse it and return a dictionary

    :param text_or_file_object: The multiline text block or a file-like object
    :return: a dictionary
    """
    if hasattr(text_or_file_object, "read"):
        file = text_or_file_object
    else:
        file = io.StringIO(text_or_file_object)

    # Determine the dialect
    read_position = file.tell()
    csv_dialect = csv.Sniffer().sniff(file.read(100))
    file.seek(read_position)

    # Parse
    reader = csv.reader(file, dialect=csv_dialect)
    key_values = (kv for kv in reader if kv)
    return dict(key_values)


def main():
    """Entry"""
    text = "".join(fileinput.input())
    print("Text to parse:")
    print(text)
    print("-" * 80)

    print("Parsed:")
    dict_object = parse(text)
    print(json.dumps(dict_object, indent=4))


if __name__ == "__main__":
    main()
