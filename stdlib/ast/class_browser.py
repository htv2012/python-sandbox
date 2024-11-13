#!/usr/bin/env python3
import argparse
import pathlib
import pprint
import pyclbr

parser = argparse.ArgumentParser()
parser.add_argument("full_path", type=pathlib.Path)
options = parser.parse_args()
print(options)

path_to_module = str(options.full_path.parent)
module_name = options.full_path.stem

result = pyclbr.readmodule_ex(module_name, path=[path_to_module])
pprint.pprint(result)
