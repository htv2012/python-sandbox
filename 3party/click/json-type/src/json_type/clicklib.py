import contextlib
import enum
import json
import pathlib
from typing import Any, Dict, List, Protocol, Union

import click
import yaml
import yaml.parser

JsonType = Union[Dict[Any, Any], List[Any], int, float, str]


class HasFromJson(Protocol):
    @classmethod
    def from_json(cls, data: JsonType):
        raise NotImplementedError()


def json_parse(json_object: str):
    with contextlib.suppress(json.JSONDecodeError):
        return json.loads(json_object)
    return json_object


def parse_file(text: str):
    """Parse a file specified by the text parameter.

    The text is in the format @filename[:selector].  The selector is
    optional. If specified, it selects the data within the file. This
    alllows us to create a single file which can hold multiple objects.

    Sample text:
        '@file.json'
        '@file.yaml'
        '@file.json:my_obj'

    Args:
        text: represent the file and a selector

    Returns:
        A JSON object
    """
    text = text.removeprefix("@")
    filename, _, selector = text.partition(":")
    path = pathlib.Path(filename)

    loaders = {".json": json.load, ".yaml": yaml.safe_load, ".yml": yaml.safe_load}
    if path.suffix not in loaders:
        raise ValueError(f"Unknown file type: {text}")

    with open(path, "rb") as stream:
        loader = loaders[path.suffix]
        content = loader(stream)

    if selector:
        return content[selector]
    return content


class JsonParamType(click.ParamType):
    name = "json"

    def __init__(self, cls: HasFromJson):
        super().__init__()
        self.cls = cls

    def convert(self, value, param, ctx):
        if value.startswith("@"):
            parse = parse_file
        else:
            parse = json_parse

        try:
            data = parse(value)
            return self.cls.from_json(data)
        except (
            FileNotFoundError,
            TypeError,
            ValueError,
            json.JSONDecodeError,
            yaml.parser.ParserError,
        ) as error:
            self.fail(str(error), param, ctx)


class EnumParamType(click.Choice):
    """Parse argument and return an enum member.

    click 8.1.7 does not support enum choices, so we have to write our
    own parser.
    """

    name = "enum"

    def __init__(self, cls: enum.EnumType):
        choices = [name.lower() for name in cls.__members__]
        super().__init__(choices, case_sensitive=False)
        self.cls = cls

    def convert(self, value, param, ctx):
        target: str = super().convert(value, param, ctx)

        # Instead of direct lookup cls[target], we do this to
        # handle case where enum names are not all upper case
        for name, member in self.cls.__members__.items():
            if name.lower() == target:
                return member
