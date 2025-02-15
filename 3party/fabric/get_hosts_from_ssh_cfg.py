#!/usr/bin/env python3
# whatis: Print all host names
import fabric

config = fabric.Config()
ssh_config = config.base_ssh_config

for host_name in sorted(ssh_config.get_hostnames()):
    print(f"host: {host_name}")
    host = ssh_config.lookup(host_name)
    for key, value in host.items():
        if key not in {"include", "sendenv"}:
            print(f"  {key}: {value}")

with fabric.Connection(host="ssh-sandbox"):
    pass
