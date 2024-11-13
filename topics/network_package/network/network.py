"""
Network-related functions
"""
import functools
import socket
import subprocess


def is_reachable(hostname):
    """
    Pings the IP address and return True if the address is reachable or
    False if not

    :param hostname: The host name or IP address, e.g. "10.0.0.4"
    :return: A boolean indicating the reachability
    """
    exit_code = subprocess.call(
        ["ping", "-c", "1", hostname],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return exit_code == 0


def is_reachable_on_port(hostname, port):
    """
    Attempts to connect to a host `hostname` via port `port` and
    returns True if success or False if not.

    :param hostname: The host name or IP address
    :param port: The port number, i.e. 22 for ssh, 80 for HTTP
    :return: A boolean indicating the host can be reach via the
        said port
    """
    try:
        socket.create_connection((hostname, port), timeout=5)
        return True
    except socket.error:
        return False


def is_reachable_on_service(hostname, service_name):
    """
    Attempts to connect to a host `hostname` via port `port` and
    returns True if success or False if not.

    :param hostname: The host name or IP address
    :param service_name: The name of the service, e.g. 'ssh'
    :return: A boolean indicating the host can be reach via the
        said port
    """
    port = socket.getservbyname(service_name)
    result = is_reachable_on_port(hostname, port)
    return result


ping = is_reachable
is_reachable_ssh = functools.partial(is_reachable_on_port, port=22)
is_reachable_web = functools.partial(is_reachable_on_port, port=80)
