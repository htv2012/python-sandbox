from datetime import datetime

import pytest
from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


@pytest.mark.parametrize(
    "data",
    [
        pytest.param(
            {"id": 1234, "signup_ts": "2026-04-29 14:35", "tastes": {}}, id="minimal"
        ),
        pytest.param(
            {
                "id": 1234,
                "name": "Anna Anderson",
                "signup_ts": "2026-04-29 14:35",
                "tastes": {
                    "books": 10,
                    "movies": 9,
                },
            },
            id="full",
        ),
    ],
)
def test_valid_user(data):
    User(**data)


@pytest.mark.parametrize(
    "data",
    [
        pytest.param({}, id="empty"),
        pytest.param(
            {"id": "one", "tastes": {}},
            id="invalid type",
        ),
    ],
)
def test_invalid_user(data):
    with pytest.raises(ValidationError):
        User(**data)
