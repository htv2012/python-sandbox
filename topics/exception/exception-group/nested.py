#!/usr/bin/env python3
from banner import banner


def verify_user(uid, alias, shell, permissions):
    account_faults = []
    if uid < 501:
        account_faults.append(ValueError(f"Expect UID>=501, got {uid!r}"))
    if alias == "root":
        account_faults.append(ValueError("Expect non-root user"))
    allowed = {"bash", "rsh", "sh", "zsh"}
    if shell not in allowed:
        account_faults.append(ValueError(f"Shell is not in allowed list: {allowed}"))

    group_exceptions = [
        ValueError(f"Not in {group!r} group")
        for group in ["reporter", "executor", "runner"]
        if group not in permissions
    ]

    if account_faults or group_exceptions:
        raise ExceptionGroup(
            f"User verification failed for user {alias}",
            [
                ExceptionGroup("Account verification failed", account_faults),
                ExceptionGroup("Permissions verification failed", group_exceptions),
            ],
        )


def main():
    banner("Demo: See what a nested ExceptionGroup looks like in the terminal")
    verify_user(uid=0, alias="root", shell="dash", permissions={"Delete Account", "Set System Time"})


if __name__ == "__main__":
    main()
