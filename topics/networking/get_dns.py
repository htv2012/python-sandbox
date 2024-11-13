#!/usr/bin/env python3
"""
Given an IP address of a controller, get the DNS servers
"""
import argparse
import csv

import paramiko


def get_dns(host, port, username, password):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        _, stdout, stderr = ssh.exec_command("nmcli connection show mgmt-fixed | awk '/ipv4.dns:/ { print $2 }'")
        reader = csv.reader(stdout)
        dns_servers = next(reader)
    return dns_servers


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", default="root")
    parser.add_argument("-p", "--password", default="default")
    parser.add_argument("ip")
    options = parser.parse_args()
    dns_servers = get_dns(options.ip, 22, options.username, options.password)
    print("\n".join(dns_servers))


if __name__ == "__main__":
    main()

