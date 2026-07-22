import argparse
import functools
import json
import pathlib


@functools.singledispatch
def print_tree(data, prefix: str = ""):
    raise NotImplementedError(f"Not implemented for type {type(data)}: {data}")


@print_tree.register
def _(data: pathlib.Path, prefix: str = ""):
    print(data.name)
    _print_fs_dir(data, prefix)


@print_tree.register
def _(data: list, prefix: str = ""):
    count = len(data)

    for i, entry in enumerate(data):
        is_last = (i == count - 1)
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
        is_last = (i == count - 1)
        connector = "└── " if is_last else "├── "

        if isinstance(value, (list, dict)):
            print(f"{prefix}{connector}{key}")
            extension = "    " if is_last else "│   "
            print_tree(value, prefix + extension)
        else:
            print(f"{prefix}{connector}{key}={value!r}")


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
    parser.add_argument("path")
    options = parser.parse_args()

    path = pathlib.Path(options.path)
    if path.is_dir():
        print_tree(path)
    else:
        if path.suffix == ".json":
            with open(path) as stream:
                data = json.load(stream)
        else:
            raise SystemExit(f"File type not supported: {path}")
        print_tree(data)


if __name__ == "__main__":
    main()
