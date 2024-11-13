#!/usr/bin/env python
import boto3


def main():
    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket("sandbox-haiku")

    for entry in bucket.objects.iterator():
        print(entry)


if __name__ == '__main__':
    main()
