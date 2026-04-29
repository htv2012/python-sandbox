from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError

from .banner import banner


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


def valid_data_example():
    banner("Happy path, validation succeeded")

    data = {
        "id": 1234,
        "signup_ts": "2026-04-29 14:35",
        "tastes": {
            "wine": 9,
            "cheese": 8,
            "cabbage": 1,
        },
    }
    user = User(**data)

    print(f"{user.id        = }")
    print(f"{user.name      = }")
    print(f"{user.signup_ts = }")
    print(f"{user.tastes    = }")


def missing_id_example():
    banner("Missing ID")

    data = {
        "signup_ts": "2026-04-29 14:35",
        "tastes": {
            "wine": 9,
            "cheese": 8,
            "cabbage": 1,
        },
    }

    try:
        User(**data)
    except ValidationError as err:
        print(err)


def multiple_validation_errors_example():
    banner("Multiple errors")

    data = {
        "name": ["John", "Doe"],
        "signup_ts": "2026-04-29 14:35",
        "tastes": {
            "wine": 9,
            "cheese": 8,
            "cabbage": "yuk",
        },
    }

    try:
        User(**data)
    except ValidationError as err:
        print(err)


def ex1():
    valid_data_example()
    missing_id_example()
    multiple_validation_errors_example()
