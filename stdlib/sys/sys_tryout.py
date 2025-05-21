#!/usr/bin/env python3
"""
A Python skeleton script
"""

import sys
from pprint import pprint


def pretty_print(tag, value):
    print(f"\n# {tag}")
    if isinstance(value, (str, int, bool)):
        print(value)
    else:
        pprint(value)


def main():
    attrs = [
        "abiflags",
        "api_version",
        "argv",
        "base_exec_prefix",
        "base_prefix",
        "builtin_module_names",
        "byteorder",
        "call_tracing",
        "copyright",
        "dont_write_bytecode",
        "exec_prefix",
        "executable",
        "flags",
        "float_info",
        "float_repr_style",
        "hexversion",
        "implementation",
        "int_info",
        "maxsize",
        "maxunicode",
        "meta_path",
        "modules",
        "path",
        "path_hooks",
        "path_importer_cache",
        "platform",
        "prefix",
        "stderr",
        "stdin",
        "stdout",
        "thread_info",
        "version",
        "version_info",
        "warnoptions",
    ]
    for attr in attrs:
        pretty_print(attr, getattr(sys, attr))


if __name__ == "__main__":
    main()
