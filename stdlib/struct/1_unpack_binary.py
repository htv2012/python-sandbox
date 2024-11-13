#!/usr/bin/env python3
"""
A Python skeleton script
"""
import struct


def main():
    """ Entry """
    binary = bytearray(b'abcd' * 4)
    binary[8:12] = [81, 100, 1, 16]
    print(binary)

    format_string = "<xxxxxxxxLxxxx"
    print(f"Format String: {format_string!r}")

    version, = struct.unpack(format_string, binary)
    print(hex(version))

    # Parse the version:
    # bits 31..16: revision ID
    # bits 15..12: reserved
    # bits 11..0: device ID
    revision_id = version >> 16
    device_id = version & 0b111111111111

    print(f"Revision ID: 0x{revision_id:04x}")
    print(f"Device ID:   0x{device_id:04x}")


if __name__ == '__main__':
    main()

