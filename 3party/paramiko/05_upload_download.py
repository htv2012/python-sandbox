#!/usr/bin/env python3
"""
Upload a file
"""
import random
import tempfile

import sshtools


def main():
    """Entry"""
    # Connect to the remote host
    client = sshtools.connect_with_config("nuc")

    # Create a temp file, upload, download, round-trip check
    with tempfile.TemporaryFile() as file_stream, client.open_sftp() as sftp:
        file_stream.write(b"\x01\x02\x03")
        rand_byte = random.choice([b"\x05", b"\x06", b"\x07"])
        file_stream.write(rand_byte)

        # Upload
        file_stream.seek(0)
        sftp.putfo(file_stream, "/tmp/deleteme.bin")

        # Download
        sftp.get("/tmp/deleteme.bin", "/tmp/deleteme.bin")

    # Round-trip verify
    with open("/tmp/deleteme.bin", "rb") as file_stream:
        contents = file_stream.read()
        assert len(contents) == 4
        assert contents[:3] == b"\x01\x02\x03"
        assert contents[3] in {5, 6, 7}


if __name__ == "__main__":
    main()
