#!/usr/bin/env python3
"""Create exaple for make_dataclass."""
import dataclasses


def main():
    """Perform script."""
    blueprint = [
        ("uid", int),
        ("alias", str),
        ("is_admin", bool),
    ]
    User = dataclasses.make_dataclass("User", blueprint)

    user = User(uid=501, alias="karen", is_admin=True)
    assert user.uid == 501
    assert user.alias == "karen"
    assert user.is_admin is True
    print(user)


if __name__ == "__main__":
    main()
