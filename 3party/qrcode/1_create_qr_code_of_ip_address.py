#!/usr/bin/env python
"""
Prints a list of IP addresses
"""
from __future__ import print_function
import platform
import socket
import subprocess

import qrcode


# pylint: disable=line-too-long
# Sample ip -oneline address output
# 1: lo    inet 127.0.0.1/8 scope host lo\       valid_lft forever preferred_lft forever
# 1: lo    inet6 ::1/128 scope host \       valid_lft forever preferred_lft forever
# 2: eth0    inet 10.238.1.221/24 brd 10.238.1.255 scope global noprefixroute dynamic eth0\       valid_lft 78840sec preferred_lft 78840sec
# 2: eth0    inet6 fe80::250:56ff:fea8:ef1b/64 scope link \       valid_lft forever preferred_lft forever
# 3: docker0    inet 10.0.10.0/16 brd 10.0.255.255 scope global docker0\       valid_lft forever preferred_lft forever
# 3: docker0    inet6 fe80::42:19ff:fe51:877f/64 scope link \       valid_lft forever preferred_lft forever
# pylint: enable=line-too-long

def get_local_addresses_linux():
    """ Run external command and parse output to get local addresses """
    command = ['ip', '-oneline', 'address']
    try:
        output = subprocess.check_output(command, encoding='utf8')  # Py3
    except TypeError:
        output = subprocess.check_output(command)                   # Py2

    ip_addresses = [line.split()[3] for line in output.splitlines()]
    ip_addresses = [ip.split('/')[0] for ip in ip_addresses]
    return ip_addresses


def get_local_addresses(host_name):
    if platform.system() == 'Linux':
        ip_addresses = get_local_addresses_linux()
    else:
        host_name, _, ip_addresses = socket.gethostbyname_ex(host_name)

    return ip_addresses

def main():
    """ Entry point """
    host_name = socket.gethostname()
    ip_addresses = get_local_addresses(host_name)
    print(host_name, ' '.join(ip_addresses))

    # Create the QR code
    url = f"http://{host_name}:8000/"
    image = qrcode.make(url)
    image.save("url.png")


if __name__ == '__main__':
    main()

