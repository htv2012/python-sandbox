import logging
from typing import Optional

import fastapi

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


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
            }
        ]
    }


DB = {
    501: {"alias": "kevin", "shell": "bash"},
    502: {"alias": "anna", "shell": "zsh"},
}


@app.get("/users/")
def get_all():
    return DB


@app.get("/users/{user_id}")
def get_item(user_id: Optional[int] = None):
    print(f"GET user_id={user_id}")
    logging.info("GET user_id=%r", user_id)
    if user_id is None:
        return {"ids": DB.keys()}
    try:
        return DB[user_id]
    except KeyError:
        raise fastapi.HTTPException(404)
