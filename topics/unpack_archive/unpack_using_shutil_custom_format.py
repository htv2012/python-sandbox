#!/usr/bin/env python3
import pathlib
import shutil
import subprocess


def lzma_untar(archive_path, out_dir, filter=None, **kwargs):
    pathlib.Path(out_dir).mkdir(exist_ok=True)
    subprocess.run(
        [
            "tar",
            "--lzma",
            "--extract",
            "--file",
            str(archive_path),
            "--directory",
            str(out_dir),
        ],
    )


shutil.register_unpack_format(
    "lztar",
    [".tar.lz", "tar.lzma"],
    lzma_untar,
    description="LZMA tar file",
)
shutil.unpack_archive("my.tar.lz", "out")
