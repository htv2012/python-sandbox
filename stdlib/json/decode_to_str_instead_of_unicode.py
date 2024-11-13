#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Overwrite json.load to return str instead of unicode key and value"""

import json
import os
from pprint import pprint


def unicode2str_hook(dict_object):
    new_dict_object = {
        str(k): str(v) if isinstance(v, str) else v
        for k, v in list(dict_object.items())
    }
    return new_dict_object


if __name__ == "__main__":
    data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.json"
    )
    with open(data_filename) as f:
        obj = json.load(f, object_hook=unicode2str_hook)
        print("---")
        pprint(obj)
