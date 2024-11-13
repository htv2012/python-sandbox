#!/usr/bin/env python3
""""Get reference based on the type of the input.

- For a dictionary, look at key "ref"
- For a Response object, look at the .data attribute, which is a dict
- For an Api object, call .get() to get a Response object
"""
import dataclasses
from functools import singledispatch


@dataclasses.dataclass
class Response:
    data: dict


class Api:
    def get(self):
        return Response({"ref": "api1"})


class Env(Api):
    def get(self):
        return Response({"ref": "env1"})


@singledispatch
def get_ref(obj):
    raise TypeError(f"Cannot handle {obj} (type: {obj.__class__.__name__})")


@get_ref.register(dict)
def get_ref_dict(obj):
    return obj["ref"]


@get_ref.register(Response)
def get_ref_response(obj):
    return get_ref(obj.data)


@get_ref.register(Api)
def get_ref_api(obj):
    response = obj.get()
    return get_ref(response)


def tryout(obj):
    class_name = obj.__class__.__name__
    try:
        ref = get_ref(obj)
        print(f"# {class_name}: ref={ref}")
    except TypeError as error:
        print(f"{class_name}: {error}")


def main():
    """Entry"""
    data = [
        {"ref": "ref1"},
        Response({"ref": "ref2"}),
        Api(),
        Env(),
        15,
    ]
    for obj in data:
        tryout(obj)


if __name__ == "__main__":
    main()
