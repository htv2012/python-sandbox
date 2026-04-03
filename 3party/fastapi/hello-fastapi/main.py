import dataclasses
import logging

import fastapi

import model
import users

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


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
def get_users():
    """Get a list of users."""
    return [dataclasses.asdict(user) for user in users.get_all()]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get a user given an ID.

    :param user_id: The user ID
    """
    logging.info("GET user_id=%r", user_id)
    user = users.get(user_id)
    logging.info("user=%r", user)
    if user is None:
        raise fastapi.HTTPException(404)
    return dataclasses.asdict(user)


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
