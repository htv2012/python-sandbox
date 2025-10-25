#!/usr/bin/python3
import csv
import json


def no_cast(value):
    return value


def my_cast(value):
    """Cast a value by JSON decode"""
    try:
        return json.loads(value)
    except json.decoder.JSONDecodeError:
        return value


def text2dict(text: str, delimiter: str = ",", value_cast=None) -> dict:
    value_cast = value_cast or no_cast
    reader = csv.reader([text], delimiter=delimiter, skipinitialspace=True)
    key_value_list = next(reader)
    kv_reader = csv.reader(key_value_list, delimiter=":", skipinitialspace=True)
    result = dict(kv_reader)
    result = {key.strip(): value_cast(value) for key, value in result.items()}
    return result


def main():
    text_list = [
        ("uid: 501, alias: anna, shell: zsh, is_admin: false", ","),
        ('tower : 103 | rx : 1.5 | tx : 3.1 | note : "First contact"', "|"),
    ]

    for text, delim in text_list:
        print(text)
        result = text2dict(text, delim, value_cast=my_cast)
        print(json.dumps(result, indent=4))
        print()


if __name__ == "__main__":
    main()
