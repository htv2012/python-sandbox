# List all functions declared in a Python module
# Syntax:
#   python list_functions_in_a_module.py dirwalk.py


import importlib
import logging
import os
import sys
from inspect import getmembers, isfunction


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("LIST_FUNCTIONS")

    file_name = sys.argv[1]
    module_name = os.path.splitext(file_name)[0]
    logger.debug("file:   {0}".format(file_name))
    logger.debug("module: {0}".format(module_name))

    mod = importlib.import_module(module_name)
    functions_list = getmembers(mod, isfunction)
    print("\n".join([x[0] for x in functions_list]))


if __name__ == "__main__":
    main()
