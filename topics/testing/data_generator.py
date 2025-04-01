#!/usr/bin/env python

import itertools
import json

# import yaml


def data_generator(**kwargs):
    keys = list(kwargs.keys())
    for value in itertools.product(*list(kwargs.values())):
        yield dict(list(zip(keys, value)))


def repr_dict(dict_object):
    keys_values = ", ".join("%r: %r" % (k, dict_object[k]) for k in sorted(dict_object))
    return "{" + keys_values + "}"


if __name__ == "__main__":
    data = data_generator(
        datasource=["relational", "cube"],
        sheet_type=["worksheet", "dashboard", "storyboard"],
        selection=["single", "multiple"],
    )
    test_cases = {
        "{datasource}_datasource_{selection}_selection_from_{sheet_type}".format(
            **tc
        ): tc
        for tc in data
    }

    print(json.dumps(test_cases, indent=4, sort_keys=True))
    # print(yaml.dump(test_cases, indent=4))
