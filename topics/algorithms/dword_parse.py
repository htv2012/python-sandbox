#!/usr/bin/env python3
"""
Splits a DWORD into parts
"""
import sys


def unpack_dword(dword, *indices):
    for index in indices:
        lower, upper = sorted(int(x) for x in index.split(".."))
        shifted = dword >> lower
        mask = (1 << (upper - lower + 1)) - 1
        yield shifted & mask


def main():
    """Entry"""
    dword = int.from_bytes([81, 100, 1, 16], sys.byteorder)
    print(f"dword=0x{dword:08x}")
    revision_id, device_id = unpack_dword(dword, "31..16", "0..11")
    print(f"Revision ID: 0x{revision_id:04x}")
    print(f"Device ID:   0x{device_id:04x}")


if __name__ == "__main__":
    main()
