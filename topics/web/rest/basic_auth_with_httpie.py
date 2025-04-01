#!/usr/bin/env python3
"""
Demo: Basic auth with httpie (http and https commands)
"""

import json
import subprocess


def get(url, username, password):
    """GET url with basic auth."""
    cmd = ["https", "--auth", f"{username}:{password}", "--print=b", url]
    completed_process = subprocess.run(
        cmd, check=False, encoding="utf-8", capture_output=True
    )
    return completed_process.stdout


def main():
    """Entry"""
    raw = get(
        "https://pie.dev/basic-auth/user1/user1Password", "user1", "user1Password"
    )
    data = json.loads(raw)
    print(data)


if __name__ == "__main__":
    main()
