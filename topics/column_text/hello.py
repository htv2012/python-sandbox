# import subprocess
import argparse
import os

from columnize import columnize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default=".")
    parser.add_argument("-w", "--width", type=int)
    options = parser.parse_args()

    files_list = [f"{i:>03}. {name}" for i, name in enumerate(os.listdir(options.dir))]
    columnize(files_list, total_width=options.width)


if __name__ == "__main__":
    main()
