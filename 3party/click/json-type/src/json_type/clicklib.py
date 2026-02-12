import contextlib
import enum
import json
import pathlib
from typing import Any, Dict, List, Optional, Protocol, Union, override

import click
import yaml
import yaml.parser

JsonType = Union[Dict[Any, Any], List[Any], int, float, str]


class HasFromJson(Protocol):
    @classmethod
    def from_json(cls, json_object: JsonType):
        raise NotImplementedError()  # pragma: no cover


def json_parse(json_str: str):
    """Parse JSON, if failed, return the original object.

    Args:
        json_str: The string presentation of a JSON object

    Returns:
        A JSON object
    """
    with contextlib.suppress(json.JSONDecodeError):
        return json.loads(json_str)
    return json_str


def parse_file(file_spec: str):
    """Parse a file specified by the file_spec parameter.

    The file_spec is in the format @filename[:selector].  The selector is
    optional. If specified, it selects the data within the file. This
    alllows us to create a single file which can hold multiple objects.

    Example 1. Using the argument "@file1.yaml" will return {"uid": 501, "alias": "anna"}::

        # file1.yaml
        uid: 501
        alias: anna

    Example 2. Using the argument "@file2.yaml:user1" will return the same data::

        # file2.yaml
        user1:
            uid: 501
            alias anna
        user2:
            uid: 502
            alias karen

    Args:
        file_spec: represent the file and a selector

    Returns:
        A JSON object
    """
    file_spec = file_spec.removeprefix("@")
    filename, _, selector = file_spec.partition(":")
    path = pathlib.Path(filename)

    loaders = {".json": json.load, ".yaml": yaml.safe_load, ".yml": yaml.safe_load}
    loader = loaders.get(path.suffix)
    if loader is None:
        raise ValueError(f"Unknown file type: {file_spec}")

    with open(path, "rb") as stream:
        content = loader(stream)

    if selector:
        return content[selector]
    return content


class JsonParamType(click.ParamType):
    """Parameter type which converts a JSON string into objects.

    Args:
        cls: The class to be returned. It must have a class method named
            `from_json`. If not specified, the convert method will return
            the raw JSON object.
    """

    name = "json"

    def __init__(self, cls: Optional[HasFromJson] = None):
        name = getattr(cls, "__name__", None)
        if not (cls is None or name is None):
            self.name = name

        super().__init__()
        self.cls: Optional[HasFromJson] = cls

    @override
    def convert(self, value: str, param, ctx):
        parse = parse_file if value.startswith("@") else json_parse
        try:
            json_object = parse(value)
            if self.cls is None:
                return json_object
            return self.cls.from_json(json_object)
        except (
            FileNotFoundError,
            TypeError,
            ValueError,
            json.JSONDecodeError,
            yaml.parser.ScannerError,
            yaml.parser.ParserError,
        ) as error:
            self.fail(str(error), param, ctx)


class EnumParamType(click.Choice):
    """Parse argument and return an enum member.

    click 8.1.7 does not support enum choices, so we have to write our
    own parser.
    """

    def __init__(self, cls: enum.EnumType):
        self.name = cls.__name__
        choices = [name.lower() for name in cls.__members__]
        super().__init__(choices, case_sensitive=False)
        self.cls = cls

    @override
    def convert(self, value: str, param, ctx):
        target: str = super().convert(value, param, ctx)

        # Instead of direct lookup cls[target], we do this to
        # handle case where enum names are not all upper case
        for name, member in self.cls.__members__.items():
            if name.lower() == target:
                return member
