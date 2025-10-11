#!/usr/bin/env python3
from banner import banner


def verify_user(user: dict):
    excs = []
    if user["uid"] < 501:
        excs.append(ValueError(f"Expect UID>=501, got {user['uid']!r}"))
    if user["alias"] == "root":
        excs.append(ValueError("Expect non-root user"))
    allowed = {"bash", "rsh", "sh", "zsh"}
    if user["shell"] not in allowed:
        excs.append(ValueError(f"Shell is not in allowed list: {allowed}"))

    if excs:
        raise ExceptionGroup("User verification failed", excs)


def main():
    banner("Demo: See what an ExceptionGroup looks like in the terminal")
    user = dict(uid=0, alias="root", shell="dash")
    verify_user(user)


if __name__ == "__main__":
    main()
