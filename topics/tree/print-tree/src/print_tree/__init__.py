import argparse
import collections
import functools
import pathlib


@functools.singledispatch
def print_tree(data):
    raise NotImplementedError(f"Not implemented for type {type(data)}: {data}")


@print_tree.register
def _(data: pathlib.Path):
    print(data.name)
    _print_fs_dir(data)


@print_tree.register
def _(data: list):
    print(data)
    print("under construction")


def _print_fs_dir(path: pathlib.Path, prefix: str = ""):
    entries = sorted(path.iterdir(), key=lambda p: p.name.lower())
    count = len(entries)

    for i, entry in enumerate(entries):
        is_last = i == count - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            # Extend prefix with spaces if this dir was last, otherwise keep the pipe
            extension = "    " if is_last else "│   "
            _print_fs_dir(entry, prefix + extension)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    options = parser.parse_args()

    root = pathlib.Path(options.root)
    if not root.is_dir():
        raise SystemExit(f"{root} is not a directory.")
    print_tree(root)


if __name__ == "__main__":
    main()