import dataclasses
import itertools
import logging
from typing import Optional

import fastapi

import model

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
IDS_POOL = itertools.count(503)


def get(uid: int) -> User:
    for user in USERS:
        if uid == user.uid:
            return user
    return None


def get_all():
    return USERS


def create(user_data: model.UserCreate) -> int:
    for user in USERS:
        if user.alias == user_data.alias:
            raise ValueError()
    uid = next(IDS_POOL)
    USERS.append(User(uid, user_data.alias, user_data.shell, user_data.is_admin))
    return uid


def delete(uid: int):
    for i, user in enumerate(USERS):
        if user.uid == uid:
            del USERS[i]
            return
    raise LookupError()


def update(uid: int, update_data: model.UserUpdate):
    valid_shells = {"zsh", "bash", "dash", "tcsh", "sh"}
    for user in USERS:
        if user.uid == uid:
            if update_data.shell is not None:
                if update_data.shell not in valid_shells:
                    raise ValueError(
                        f"Shell must be one of {', '.join(valid_shells)}, got {update_data.shell}"
                    )
                user.shell = update_data.shell
            if update_data.is_admin is not None:
                user.is_admin = update_data.is_admin
            break
    else:
        raise LookupError("User not found")
