#!/usr/bin/env python3
"""
A Python skeleton script
"""
from pprint import pprint
import sys


def pretty_print(tag, value):
    print(tag, end="")
    pprint(value)


def main():
    """ Entry """
    pretty_print("abiflags =", sys.abiflags)
    pretty_print("api_version =", sys.api_version)
    pretty_print("argv =", sys.argv)
    pretty_print("base_exec_prefix =", sys.base_exec_prefix)
    pretty_print("base_prefix =", sys.base_prefix)
    pretty_print("builtin_module_names =", sys.builtin_module_names)
    pretty_print("byteorder =", sys.byteorder)
    pretty_print("call_tracing =", sys.call_tracing)
    pretty_print("copyright =", sys.copyright)
    pretty_print("dont_write_bytecode =", sys.dont_write_bytecode)
    pretty_print("exec_prefix =", sys.exec_prefix)
    pretty_print("executable =", sys.executable)
    pretty_print("flags =", sys.flags)
    pretty_print("float_info =", sys.float_info)
    pretty_print("float_repr_style =", sys.float_repr_style)
    pretty_print("hexversion =", hex(sys.hexversion))
    pretty_print("implementation =", sys.implementation)
    pretty_print("int_info =", sys.int_info)
    pretty_print("maxsize =", sys.maxsize)
    pretty_print("maxunicode =", sys.maxunicode)
    pretty_print("meta_path =", sys.meta_path)
    pretty_print("modules =", sys.modules)
    pretty_print("path =", sys.path)
    pretty_print("path_hooks =", sys.path_hooks)
    pretty_print("path_importer_cache =", sys.path_importer_cache)
    pretty_print("platform =", sys.platform)
    pretty_print("prefix =", sys.prefix)
    pretty_print("stderr =", sys.stderr)
    pretty_print("stdin =", sys.stdin)
    pretty_print("stdout =", sys.stdout)
    pretty_print("thread_info =", sys.thread_info)
    pretty_print("version =", sys.version)
    pretty_print("version_info =", sys.version_info)
    pretty_print("warnoptions =", sys.warnoptions)


if __name__ == '__main__':
    main()

