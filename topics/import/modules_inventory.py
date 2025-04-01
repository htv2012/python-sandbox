#!/usr/bin/env python
"""Which module is available?"""

import importlib

module_names = """
arrow
boltons
bottle
bs4
colorama
colorlog
hug
json
parsedatetime
psutil
ptpython
pyqt
pyqtgraph
pywebview
readline
requests
rlcompleter
watchdog
yaml
""".split()


if __name__ == "__main__":
    for module_name in module_names:
        try:
            importlib.import_module(module_name)
            print("🗸", module_name)
        except ImportError:
            print(" ", module_name)
