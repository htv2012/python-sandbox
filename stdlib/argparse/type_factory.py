"""
Demo: the type=xxx from the add_argument() call can accept any callable
that takes a string and return a value. This script demonstrates that.
"""

import argparse
import socket
import ipaddress


def get_port(port):
    try:
        return int(port)
    except ValueError:
        pass

    try:
        return socket.getservbyname(port)
    except OSError:
        return port


def get_ip_address(host):
    try:
        return ipaddress.ip_address(host)
    except ValueError:
        pass

    address = socket.gethostbyname(host)
    return ipaddress.ip_address(address)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=get_port)
    print(parser.parse_args(["ssh"]))
    print(parser.parse_args(["22"]))

    parser = argparse.ArgumentParser()
    parser.add_argument("ip", type=get_ip_address)
    print("---")
    print(parser.parse_args(["10.0.0.5"]))
    print(parser.parse_args(["haimacbookair.local"]))
    print(parser.parse_args(["google.com"]))
