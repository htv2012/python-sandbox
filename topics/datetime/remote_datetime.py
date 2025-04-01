#!/usr/bin/env python3
"""
Gets and parse remote date/time
"""

import datetime

try:
    import paramiko
except ImportError:
    print("Please install paramiko for this module to work")
    raise SystemExit(1)


PYTHON_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LINUX_DATE_FORMAT = f"+{PYTHON_DATE_FORMAT}"


def _get_date_output(host, port, username, password):
    with paramiko.SSHClient() as ssh:
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        _, stdout, _ = ssh.exec_command(f"date '{LINUX_DATE_FORMAT}'")

        output = stdout.read().decode("utf-8").strip()
        return output


def get_remote_date(host, port, username, password):
    date_output = _get_date_output(host, port, username, password)
    datetime_object = datetime.datetime.strptime(date_output, PYTHON_DATE_FORMAT)
    return datetime_object
