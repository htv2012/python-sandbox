#!/usr/bin/env python3
import struct

def main():
    """ Entry """
    binary = bytes([1, 2, 81, 100, 1, 16])
    unpacker = struct.Struct("<xxL")
    version, = unpacker.unpack(binary)
    print(hex(version))


if __name__ == '__main__':
    main()
