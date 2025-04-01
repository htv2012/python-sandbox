#!/usr/bin/env python3
"""Use descriptor to validate IP addresses."""

import ipaddress


class IPAddress:
    def __init__(self, value=None):
        self.value = self.validate(value)

    def validate(self, value):
        if value is None:
            return value
        return ipaddress.ip_address(value)

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, value):
        self.value = self.validate(value)


class Host:
    ip_address: IPAddress = IPAddress()

    def __init__(self, address=None):
        self.ip_address = address


def main():
    """Perform script."""
    print("\n# Host without address")
    host = Host()
    print(f"address={host.ip_address}")

    print("\n# Host with address")
    host = Host("192.168.1.1")
    print(f"address={host.ip_address}")

    print("\n# Assign an invalid IP address")
    try:
        host.ip_address = "192.168.1.256"
    except ValueError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()
