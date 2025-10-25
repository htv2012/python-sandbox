# tool.py
import contextlib
import csv
import subprocess


def parse_block(text: str):
    reader = csv.reader(text.splitlines(), delimiter="=")
    block = {}
    for key, value in reader:
        with contextlib.suppress(ValueError):
            value = int(value)
        block[key] = value
    return block


def get_block_devices():
    completed_process = subprocess.run(
        ["blkid", "--output", "udev"], capture_output=True, text=True
    )
    blocks = completed_process.stdout.split("\n\n")

    block_devices = {}
    for block_text in blocks:
        block_info_dict = parse_block(block_text)
        block_devices[block_info_dict["ID_FS_UUID_ENC"]] = block_info_dict

    return block_devices
