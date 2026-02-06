import json
import pathlib

import click
import yaml
import yaml.parser

from data import HasFromJson


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
            parse = json.loads

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
