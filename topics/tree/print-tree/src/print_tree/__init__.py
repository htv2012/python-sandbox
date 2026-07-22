import functools
import pathlib


@functools.singledispatch
def print_tree(data):
    raise NotImplementedError(f"Not implemented for type {type(data)}: {data}")


@print_tree.register
def _(data: pathlib.Path):
    _print_fs(data)


@print_tree.register
def _(data: list):
    print(data)
    print("under construction")


def _print_fs(path: pathlib.Path, prefix: str = ""):
    if path.is_file():
        #connector = "└── " if is_last else "├── "
        connector = "└── "
        print(f"{prefix}{connector}{path.name}")
        return

    nodes = list(path.glob("*"))
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node.name}")
        for sub_node in node.glob("*"):
            _print_fs(sub_node, prefix=prefix + ("    " if is_last else "│   "))
