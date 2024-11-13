#!/usr/bin/env python3
from box import Box

env = Box(
    {
        "servers": [
            {
                "ip": "10.0.0.100",
                "username": "test0",
                "password": "4getMe0!",
                "port": 7000,
            },
            {
                "ip": "10.0.0.101",
                "username": "test1",
                "password": "Def4u15",
                "port": 7001,
            },
        ]
    }
)

print("Using indices")
print(f"  {env.servers[0].username}@{env.servers[0].ip}:{env.servers[0].port}")
print(f"  {env.servers[1].username}@{env.servers[1].ip}:{env.servers[1].port}")


print("---")
print("Using loop")
for server in env.servers:
    print(f"  {server.username}@{server.ip}:{server.port}")
