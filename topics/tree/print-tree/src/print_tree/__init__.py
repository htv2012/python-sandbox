import functools
import pathlib
import xml.etree.ElementTree as ET


@functools.singledispatch
def print_tree(data, prefix: str = ""):
    raise NotImplementedError(f"Not implemented for type {type(data)}: {data}")


@print_tree.register
def _(data: list, prefix: str = ""):
    count = len(data)

    for i, entry in enumerate(data):
        is_last = i == count - 1
        connector = "└── " if is_last else "├── "

        if isinstance(entry, (list, dict)):
            print(f"{prefix}{connector}[{i}]")
            extension = "    " if is_last else "│   "
            print_tree(entry, prefix + extension)
        else:
            print(f"{prefix}{connector}[{i}]={entry!r}")


@print_tree.register
def _(data: dict, prefix: str = ""):
    count = len(data)

    for i, (key, value) in enumerate(data.items()):
        is_last = i == count - 1
        connector = "└── " if is_last else "├── "

        if isinstance(value, (list, dict)):
            print(f"{prefix}{connector}{key}")
            extension = "    " if is_last else "│   "
            print_tree(value, prefix + extension)
        else:
            print(f"{prefix}{connector}{key}={value!r}")


def format_node(node: ET.Element):
    text = (node.text or "").strip()
    attributes = ", ".join(f"{k}={v!r}" for k, v in node.items())
    if attributes:
        attributes = f"  # {attributes}"

    if text:
        out = f"{node.tag}={text!r}{attributes}"
    else:
        out = f"{node.tag}{attributes}"
    return out


@print_tree.register
def _(data: ET.ElementTree, prefix: str = ""):
    root = data.getroot()
    assert root is not None
    print(f"{prefix}{format_node(root)}")
    print_tree(root)


@print_tree.register
def _(data: ET.Element, prefix: str = ""):
    nodes = list(data)
    count = len(nodes)

    for i, node in enumerate(nodes):
        is_last = i == count - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "
        print(f"{prefix}{connector}{format_node(node)}")
        print_tree(node, prefix + extension)


@print_tree.register
def _(data: pathlib.Path, prefix: str = ""):
    entries = sorted(data.iterdir(), key=lambda p: p.name)
    count = len(entries)

    for i, entry in enumerate(entries):
        is_last = i == count - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(entry, prefix + extension)
