#!/usr/bin/env python
# detab.py: tool to expand tab to spaces
# Example:
#     detab myfile.py
#
# History
#   2008-01-12 first version
#
# Known Bugs
#   - expandtabs() seems to expand tabs within the quotes. We don't want that.
#

import os
import shutil
import sys


def usage():
    print("Usage: detab filename")


def replaceExtension(originalFile, newExtension):
    fileNumber = 1
    while True:
        newFile = "%s.%03d%s" % (originalFile, fileNumber, newExtension)
        if not os.path.exists(newFile):
            break
        fileNumber = fileNumber + 1
    return newFile


def main():
    # Verify the command line
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    # Create a backup file
    srcFile = sys.argv[1]
    bakFile = replaceExtension(srcFile, ".bak")
    shutil.copyfile(srcFile, bakFile)

    inFile = open(bakFile, "r")
    outFile = open(srcFile, "w")

    # process the file
    for text in inFile:
        outFile.write(text.expandtabs(4))

    inFile.close()
    outFile.close()


if __name__ == "__main__":
    main()
