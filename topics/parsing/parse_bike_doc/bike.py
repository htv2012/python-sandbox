import html.parser
import io
import json
import logging
import pathlib
import xml.etree.ElementTree


def _parse_outline(root: xml.etree.ElementTree.Element):
    out = {}
    for node in root.findall("outline"):
        text = node.attrib.get("text")
        if text is None:
            continue
        out[node.attrib.get("text")] = _parse_outline(node)
    return out


def _format_outline(outline):
    def format_it(dict_object: dict, level: int, file_object):
        for text, sub_dict in dict_object.items():
            file_object.write(f"{'    ' * level}- {text}\n")
            format_it(sub_dict, level + 1, file_object)

    buffer = io.StringIO()
    format_it(outline, 0, buffer)
    return buffer.getvalue()


def print_outline(outline: dict):
    print(_format_outline(outline))


class _BikeParser(html.parser.HTMLParser):
    def __init__(self, *args, **kwargs):
        self.level = -1
        self.stack = [{}]
        self.text_found = False
        super().__init__(*args, **kwargs)

    @property
    def outline(self):
        return self.stack[0]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "ul":
            self.level += 1
            logging.debug("<ul> - level=%r", self.level)
        elif tag == "p":
            self.text_found = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "ul":
            self.level -= 1
            logging.debug("</ul> - level=%r", self.level)
        elif tag == "p":
            self.text_found = False

    def handle_data(self, data: str) -> None:
        if not self.text_found:
            return

        text = data.strip()
        next_level = {}
        while len(self.stack) > self.level + 1:
            self.stack.pop()
        self.stack[-1][text] = next_level
        self.stack.append(next_level)

        logging.debug("data, level=%r, data=%r", self.level, data.rstrip())
        logging.debug(json.dumps(self.stack[0], indent=4))


def parse_bike_opml(full_path: str):
    doc = xml.etree.ElementTree.parse(full_path)
    root = doc.getroot()
    body = root.find(".//body")
    outline = _parse_outline(body)
    return outline


def _parse_bike_bike(full_path: str):
    parser = _BikeParser()
    with open(full_path) as stream:
        parser.feed(stream.read())
    return parser.outline


def parse_bike(full_path: str):
    full_path = pathlib.Path(full_path)
    if full_path.suffix == ".bike":
        return _parse_bike_bike(full_path)
    elif full_path.suffix == ".opml":
        return parse_bike_opml(full_path)
    raise ValueError(f"Invalid extension: {full_path}")
