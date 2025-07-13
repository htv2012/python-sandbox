import collections
import json

import click

ArgsKwargs = collections.namedtuple("ArgsKwargs", "args,kwargs")


def jsonify(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


class ArgsKwargsParamType(click.ParamType):
    def parse_token(self, token, args, kwargs, param, ctx):
        if "=" in token:
            kv = token.split("=")
            if len(kv) != 2:
                self.fail(f"Invalid argument: {token}", param, ctx)
            key, value = kv
            kwargs[key] = jsonify(value)
        else:
            args.append(jsonify(token))

    def convert(self, value, param, ctx):
        args = []
        kwargs = {}
        for token in value.split(","):
            self.parse_token(token, args, kwargs, param, ctx)
        return ArgsKwargs(args=args, kwargs=kwargs)


class ClassParamType(ArgsKwargsParamType):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def convert(self, value, param, ctx):
        args, kwargs = super().convert(value, param, ctx)
        try:
            return self.cls(*args, **kwargs)
        except ValueError:
            self.fail(f"Invalid arg: {value} for class {self.cls.__name__}")
