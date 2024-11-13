#!/usr/bin/env python
import argparse
import pathlib

import boto3

import s3
import filters


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filter", type=lambda x: getattr(filters, x))
    parser.add_argument("bucket_name")
    parser.add_argument("local_dir")
    options = parser.parse_args()
    return options


def main():
    options = parse_command_line()
    s3.download_all(options.bucket_name, options.local_dir, filter=options.filter)


if __name__ == "__main__":
    main()
