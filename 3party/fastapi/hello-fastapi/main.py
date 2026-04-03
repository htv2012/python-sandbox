import dataclasses
import enum
import logging
from typing import Optional

import fastapi

import model
import users

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


class GetFormat(enum.StrEnum):
    UID = "uid"
    ALIAS = "alias"
    SHORT = "short"
    FULL = "full"


def apply_format(user: users.User, format: GetFormat):
    if format == GetFormat.UID:
        return user.uid
    elif format == GetFormat.ALIAS:
        return user.alias
    elif format == GetFormat.SHORT:
        return {"uid": user.uid, "alias": user.alias}
    elif format == GetFormat.FULL:
        return dataclasses.asdict(user)


@app.get("/")
def get_help():
    """Get a list of endpoints."""
    return {
        "endpoints": [
            {
                "name": "GetUsers",
                "path": "/users/",
            },
            {
                "name": "GetUser",
                "path": "/users/{user_id}",
            },
        ]
    }


@app.get("/users/")
def get_users(format: Optional[GetFormat] = None):
    """Get a list of users."""
    if format is None:
        format = GetFormat.UID

    ret = [apply_format(user, format) for user in users.get_all()]
    return ret


@app.get("/users/{user_id}")
def get_user(user_id: int, format: Optional[GetFormat] = None):
    """Get a user given an ID.

    :param user_id: The user ID
    """
    if format is None:
        format = GetFormat.FULL

    logging.info("GET user_id=%r, format=%s", user_id, format)
    user = users.get(user_id)
    logging.info("user=%r", user)
    if user is None:
        raise fastapi.HTTPException(404)
    return apply_format(user, format)


@app.post("/users")
def create_user(user_data: model.UserCreate):
    try:
        uid = users.create(user_data)
        return {"uid": uid}
    except ValueError:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail={"reason": "Duplicate alias"},
        )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        users.delete(user_id)
    except LookupError:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail={"reason": "ID not found"},
        )
