#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Idea: encapsulate the configuration file and command-line parsing
into a single object.
"""


import argparse
import os
import yaml


class Options(object):
    def __init__(self, config_filename=None, **kwargs):
        # Load config file
        with open(config_filename) as file_handle:
            config = yaml.load(file_handle)
            config.update(kwargs)

        # Override the configuration file values
        for name, value in list(config.items()):
            setattr(self, name, value)

    def parse_args(self, arguments=None):
        parser = argparse.ArgumentParser()
        parser.add_argument("--host")
        parser.add_argument("--port", default=8888, type=int)
        parser.parse_args(arguments, namespace=self)
        return self

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        return "\n".join(
            "{}: {!r}".format(k, v) for k, v in list(self.__dict__.items())
        )


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    configuration_filename = os.path.join(script_dir, "parse_to_object.yaml")
    options = Options(config_filename=configuration_filename)
    options.parse_args()
    print(options)
