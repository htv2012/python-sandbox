"""
S3 services
"""
import multiprocessing
import pathlib

import boto3
from botocore.exceptions import ClientError

import filters
import logger


def download(bucket_name, remote_path, local_path):
    logger.debug(
        f"download:"
        f" bucket_name={bucket_name}"
        f", remote_path={remote_path}"
        f", local_path={local_path}"
    )
    # Create local dir if needed
    local_dir = pathlib.Path(local_path).parent
    local_dir.mkdir(parents=True, exist_ok=True)

    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket(bucket_name)
    bucket.download_file(remote_path, str(local_path))


def download_all(bucket_name, dest, filter=None):
    dest = pathlib.Path(dest)
    dest.mkdir(parents=True, exist_ok=True)

    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket(bucket_name)

    filter = filter or filters.is_file
    params = (
        (bucket_name, e.key, dest / e.key)
        for e in bucket.objects.all()
        if filter(e)
    )
    with multiprocessing.Pool() as pool:
        pool.starmap(download, params)

