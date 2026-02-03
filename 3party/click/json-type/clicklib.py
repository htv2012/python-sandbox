import json

import click


class JsonParamType(click.ParamType):
    name = "json"

    def __init__(self, cls):
        super().__init__()
        self.cls = cls

    def convert(self, value, param, ctx):
        try:
            kwargs = json.loads(value)
        except json.JSONDecodeError as error:
            self.fail(error, param, ctx)

        try:
            return self.cls(**kwargs)
        except TypeError as error:
            self.fail(error, param, ctx)
