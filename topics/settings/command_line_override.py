#!/usr/bin/env python

import argparse

import settings


def main():
    options = settings.Settings()

    parser = argparse.ArgumentParser(description="Options override")
    parser.add_argument("-u", "--user")
    parser.add_argument("-i", "--id", dest="uid", type=int)
    parser.add_argument("-s", "--shell", default="bash")
    parser.parse_args(namespace=options)

    print(options)


if __name__ == "__main__":
    main()
