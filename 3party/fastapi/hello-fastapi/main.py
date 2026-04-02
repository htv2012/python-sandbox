import dataclasses
import logging
from typing import Optional

import fastapi

import users

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    is_admin: bool
    shell: str


@app.get("/")
def get_index():
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
def get_all():
    return [dataclasses.asdict(user) for user in users.get_all()]


@app.get("/users/{user_id}")
def get_item(user_id: Optional[int] = None):
    logging.info("GET user_id=%r", user_id)
    user = users.get(user_id)
    logging.info("user=%r", user)
    if user is None:
        raise fastapi.HTTPException(404)
    return dataclasses.asdict(user)
