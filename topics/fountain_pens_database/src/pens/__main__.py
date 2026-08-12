import argparse

from . import data
from .shell import interactive_shell


def main():
    parser = argparse.ArgumentParser(prog="pens")
    parser.add_argument("-f", "--force-download", default=False, action="store_true")
    args = parser.parse_args()

    df = data.read(force_download=args.force_download)
    interactive_shell(df)


if __name__ == "__main__":
    main()
