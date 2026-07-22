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
    que = collections.deque([(path, "", False)])
    while que:
        node, prefix, is_last = que.popleft()
        connector = "└── " if is_last else "├── "
        if node.is_file():
            print(f"{prefix}{connector}{node.name}")
        else:
            print(f"{prefix}{connector}{node.name}")
            files = sorted(node.glob("*"), reverse=True)
            for i, sub_node in enumerate(files):
                que.appendleft((sub_node, ("    " if i == 0 else "│   ")+prefix, i==0))

