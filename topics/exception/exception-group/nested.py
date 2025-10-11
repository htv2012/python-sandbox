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

    group_excs = []
    for group in ["reporter", "executor", "runner"]:
        if group not in user["groups"]:
            group_excs.append(ValueError(f"Not in {group!r} group"))

    if excs or group_excs:
        raise ExceptionGroup(
            f"User verification failed for user {user!r}",
            [
                ExceptionGroup("Account verification failed", excs),
                ExceptionGroup("Group verification failed", group_excs),
            ],
        )


def main():
    banner("Demo: See what a nested ExceptionGroup looks like in the terminal")
    user = dict(uid=0, alias="root", shell="dash", groups={"a", "b"})
    verify_user(user)


if __name__ == "__main__":
    main()
