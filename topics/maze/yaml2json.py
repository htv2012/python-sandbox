#!/usr/bin/env python
import json
import os

import yaml

# root = os.path.dirname(os.path.abspath(__file__))
# infilename = os.path.join(root, 'maze_test_cases.yaml')
# outfilename = os.path.join(root, 'maze_test_cases.json')


def yaml2json(yaml_filename, json_filename=None):
    if json_filename is None:
        base_name, _ = os.path.splitext(yaml_filename)
        json_filename = base_name + ".json"

    with open(yaml_filename) as infile, open(json_filename, "wb") as outfile:
        test_cases = yaml.load(infile)
        json.dump(test_cases, outfile)
