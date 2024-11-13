#!/usr/bin/env python3
import io
import json

from class_serializer import serialize_object
from command import Command
from user import User


def main():
    """Entry"""
    json_object = {
        "users": [
            User(uid=501, alias="karen"),
            User(uid=502, alias="john"),
        ],
        "commands": [
            Command(uid=501, command="ls /bin", code=0, result="bin etc var"),
            Command(uid=502, command="rm /foo", code=1, result=""),
        ],
    }

    buffer = io.StringIO()
    json.dump(json_object, buffer, indent=4, default=serialize_object)
    print(buffer.getvalue())


if __name__ == "__main__":
    main()
