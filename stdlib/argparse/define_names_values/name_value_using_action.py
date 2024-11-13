#!/usr/bin/env python3
import argparse
import contextlib
import json


class JsonKeyValueAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        dict_object = getattr(namespace, self.dest) or {}
        setattr(namespace, self.dest, dict_object)

        for key_value in values:
            key, _, value = key_value.partition("=")
            with contextlib.suppress(json.decoder.JSONDecodeError):
                value = json.loads(value)
            if value == "":
                dict_object[key] = True
            else:
                dict_object[key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--define", nargs="+", action=JsonKeyValueAction, default={}
    )
    options = parser.parse_args()
    print("define = ", end="")
    print(json.dumps(options.define, indent=4))
