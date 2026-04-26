import json


def _load(filename: str):
    with open(f"data/{filename}") as stream:
        return json.load(stream)


users = _load("users.json")
