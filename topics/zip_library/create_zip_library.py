#!/usr/bin/env python3
"""
make the library
"""

import os
import zipfile


def main():
    """Entry"""
    os.chdir("./lib")

    with zipfile.PyZipFile("../mylib.zip", mode="w") as package:
        # Write the .pyc
        package.writepy("greet.py")

        # Write the .py
        package.write("farewell.py")


if __name__ == "__main__":
    main()
