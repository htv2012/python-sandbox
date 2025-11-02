#!/usr/bin/env python3
import argparse
import pathlib
import pprint
import pyclbr


def parse(path: pathlib.Path):
    path_to_module = str(path.parent)
    module_name = path.stem
    result = pyclbr.readmodule_ex(module_name, path=[path_to_module])
    return result


parser = argparse.ArgumentParser()
parser.add_argument("full_path", type=pathlib.Path)
options = parser.parse_args()
result = parse(options.full_path)
pprint.pprint(result)
