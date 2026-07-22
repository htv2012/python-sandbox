import functools
import pathlib


@functools.singledispatch
def print_tree(data):
    raise NotImplementedError(f"Not implemented for type {type(data)}: {data}")


@print_tree.register
def _(data: pathlib.Path):
    if data.is_dir():
        nodes = list(data.glob("*"))
    else:
        nodes = [data]
    _print_tree(
        nodes, get_value=lambda p: p.name, get_children=lambda p: list(p.glob("*"))
    )


@print_tree.register
def _(data: list):
    print(data)
    print("under construction")


def _print_tree(nodes: list, get_value, get_children, prefix: str = ""):
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{get_value(node)}")

        _print_tree(
            get_children(node),
            prefix=prefix + ("    " if is_last else "│   "),
            get_value=get_value,
            get_children=get_children,
        )
