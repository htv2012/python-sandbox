#!/usr/bin/env python
import json
import pathlib
import pprint

import boto3


def main():
    s3 = boto3.client("s3")
    listing = s3.list_objects(Bucket="sandbox-haiku")
    contents = listing["Contents"]
    pprint.pprint(contents)

    print("-" * 80)

    print("\n".join(r["Key"] for r in contents))

if __name__ == '__main__':
    main()
