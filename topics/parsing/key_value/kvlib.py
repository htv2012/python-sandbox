"""
Parses key-values block of text
"""

import csv
import io


def parse(text_or_file_object) -> dict:
    """
    Given a block of multiline text or a file-like object which represents
    lines of key/value, attempt to parse it and return a dictionary

    :param text_or_file_object: The multiline text block or a file-like object
    :return: a dictionary
    """
    try:
        text = text_or_file_object.read()
    except AttributeError:
        text = text_or_file_object

    # Sniff (guess) what the delimiter, quoting chars are
    csv_dialect = csv.Sniffer().sniff(text)

    # Create a CSV parser
    reader = csv.reader(io.StringIO(text), dialect=csv_dialect)

    # Remove the empty lines
    key_values = (kv for kv in reader if kv)

    # Turns into a dict
    return dict(key_values)
