#!/usr/bin/env python3
import contextlib
import os
import shutil
import subprocess

archive_path = "my.tar.lz"
out_dir = "out"
success = True

try:
    shutil.unpack_archive(archive_path, out_dir)
except shutil.ReadError as error:
    print(f"Unpack failed: {error}")
    success = False


if not success:
    with contextlib.suppress(FileExistsError):
        os.mkdir(out_dir)
    subprocess.run(
        [
            "tar",
            "--lzma",
            "--extract",
            "--file",
            str(archive_path),
            "--directory",
            str(out_dir),
        ]
    )
    print("Unpacked")
