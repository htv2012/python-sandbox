import dataclasses
import logging

import fastapi

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: str
    is_admin: bool


USERS = [
    User(501, "anna", "zsh", True),
    User(502, "ken", "bash", False),
]


def get(uid: int) -> User:
    for user in USERS:
        if uid == user.uid:
            return user
    return None


def get_all():
    return USERS
