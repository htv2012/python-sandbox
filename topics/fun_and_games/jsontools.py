import json


def save(obj, filename):
    with open(filename, "w") as f:
        json.dump(obj, f, sort_keys=True, indent=4)
