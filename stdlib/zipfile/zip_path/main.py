#!/usr/bin/env python3
import zipfile
import json
import pathlib
import shutil

def create_tree(root: pathlib.Path, blueprint: dict):
    for k, v in blueprint.items():
        file = root / k
        if v is None:
            file.write_text(f"# file: {file.name}\n")
        else:
            file.mkdir()
            create_tree(file, v)

def create_zip(filename: pathlib.Path):
    with open("files.json") as stream:
        blueprint = json.load(stream)

    root = pathlib.Path("root")
    root.mkdir()
    create_tree(root, blueprint)
    shutil.make_archive("files", "zip", root_dir=".", base_dir=root)
    shutil.rmtree(root)

def main():
    """ Entry """
    filename = pathlib.Path("files.zip")
    create_zip(filename)
    file1 = zipfile.Path(filename, "root/etc/file1.txt")
    print(file1.read_text())
    filename.unlink()


if __name__ == '__main__':
    main()
