import json

import pytest
from pydantic import BaseModel, EmailStr, PositiveInt, ValidationError


class User(BaseModel):
    name: str
    age: PositiveInt
    email: EmailStr


def test_valid():
    data = {
        "name": "Anna Kendrick",
        "age": 22,
        "email": "anna@email.com",
    }
    User.model_validate_json(json.dumps(data))


@pytest.mark.parametrize(
    "data",
    [
        pytest.param({}, id="empty dict"),
        pytest.param({"age": 22}, id="missing fields"),
        pytest.param(
            {"name": ["Anna", "Kendrick"], "age": 22, "email": "anna@email.com"},
            id="incorrect type",
        ),
        pytest.param(
            {"name": "Anna Kendrick", "age": -15, "email": "anna@email.com"},
            id="negative int",
        ),
        pytest.param(
            {"name": "Anna Kendrick", "age": 22, "email": "anna"}, id="invalid email"
        ),
    ],
)
def test_invalid(data):
    with pytest.raises(ValidationError):
        User.model_validate_json(json.dumps(data))
