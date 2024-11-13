#!/usr/bin/env python3
"""
Check to see if an IP address is ssh'able
"""
import argparse
import socket
import sys


def sshable(ip_address, port):
    """
    Returns 0 if the IP address is ssh'able, non-zero otherwise
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            return_code = sock.connect_ex((ip_address, port))
        except socket.gaierror:
            return_code = 1
    return return_code


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")
    parser.add_argument("-p", "--port", default=22, type=int)
    parser.add_argument("-v", "--verbose", default=False, action="store_true")
    options = parser.parse_args()

    code = sshable(options.ip, options.port)
    if code != 0 and options.verbose:
        sys.stderr.write(f"Cannot ssh to {options.ip}\n")
        sys.stderr.flush()
    return code


if __name__ == "__main__":
    sys.exit(main())

