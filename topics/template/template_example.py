#!/usr/bin/env python
import pathlib
import string

import yaml


me = pathlib.Path(__file__)
vars_path = me.with_name("vars.yaml")
template_path = me.with_name("template.txt")

with open(vars_path) as stream:
    keys_values = yaml.safe_load(stream)

with open(template_path) as stream:
    template = string.Template(stream.read())

output = template.safe_substitute(keys_values)

print(template.template)
print(output)
