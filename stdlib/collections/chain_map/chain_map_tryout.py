#!/usr/bin/env python3
import collections


def header(title):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def main():
    """Entry"""
    server = dict(host="myhost", port=4800)
    user = dict(username="johnk", password="4getme0")
    others = dict()
    config = collections.ChainMap(others, server, user)

    header("Info on the chain map")
    print(f"Config: {config}")
    print(f"- Maps: {config.maps}")
    print(f"- Parents: {config.parents}")

    header("Access the fields")
    print(f'Server: {config["host"]}:{config["port"]}')
    print(f'User: {config["username"]}')
    print(f'Shell: {config.get("shell", "unknown")}')

    header("New or updated fields happens to the front-most dict")
    config["host"] = "my-other-host"
    config["shell"] = "bash"
    print(f"Others: {others}")

    header("Add another mapping")
    config2 = config.new_child({"isAdmin": False, "groups": ["db_users", "users"]})
    print(f"New Config: {config2}")
    print(f'Is Admin: {config2["isAdmin"]}')
    print(f'Groups: {config2["groups"]}')

    header("Not a good idea to use defaultdict as the first dict")
    config3 = collections.ChainMap(
        collections.defaultdict(lambda: "unknown"),
        {"username": "karenc", "password": "i4got"},
        {"shell": "tcsh", "isAdmin": False},
    )
    print(f'User: {config3["username"]}')
    print(f'ID: {config3["id"]}')

    header("We can use defaultdict as the last dict")
    config3 = collections.ChainMap(
        {"username": "karenc", "password": "i4got"},
        {"shell": "tcsh", "isAdmin": False},
        collections.defaultdict(lambda: "unknown"),
    )
    print(f'User: {config3["username"]}')
    print(f'ID: {config3["id"]}')

    header("Inject a dict into the chain")
    config3.maps.insert(1, {"host": "gaggle.com", "username": "barrym"})
    print(f'User: {config3["username"]}')
    print(f'Host: {config3["host"]}')


if __name__ == "__main__":
    main()
