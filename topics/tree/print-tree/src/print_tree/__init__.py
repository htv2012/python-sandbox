import argparse
import collections
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


def _print_fs(path: pathlib.Path):
    que = collections.deque([(path, "", path.is_file())])
    while que:
        node, prefix, is_last = que.popleft()
        connector = "└── " if is_last else "├── "
        if node.is_file():
            print(f"{prefix}{connector}{node.name}")
        else:
            print(f"{prefix}{connector}{node.name}")
            files = sorted(node.glob("*"), reverse=True)
            for i, sub_node in enumerate(files):
                new_prefix = prefix + ("    " if i == 0 else "│   ")
                que.appendleft((sub_node, new_prefix, i==0))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    options = parser.parse_args()

    root = pathlib.Path(options.root)
    if not root.is_dir():
        raise SystemExit(f"{root} is not a directory.")
    print_tree(root)


