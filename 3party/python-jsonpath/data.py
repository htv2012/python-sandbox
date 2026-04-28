import json
import pathlib


def _load(filename: str):
    data_dir = pathlib.Path(__file__).parent / "data"
    with open(data_dir / filename) as stream:
        return json.load(stream)


aparel = _load("aparel.json")
inventory = _load("inventory.json")
users = _load("users.json")
