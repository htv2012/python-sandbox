#!/usr/bin/env python
# https://stackoverflow.com/q/48346752/459745
import argparse


def ext_check(expected_extension, openner):
    def extension(filename):
        if not filename.lower().endswith(expected_extension):
            # raise ValueError()
            raise argparse.ArgumentTypeError(
                "File {} should have extension {}".format(filename, expected_extension)
            )
        return openner(filename)

    return extension


parser = argparse.ArgumentParser()
parser.add_argument("outfile", type=ext_check(".txt", argparse.FileType("w")))

args = parser.parse_args()
args.outfile.write("Hello, world\n")
