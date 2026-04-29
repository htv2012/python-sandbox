import json
from datetime import datetime

from pydantic import BaseModel

from .banner import banner


class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class Meeting(BaseModel):
    when: datetime
    where: Address
    why: str = "No idea"


def ex2():
    banner("Show Model JSON Schema")
    print(json.dumps(Meeting.model_json_schema(), indent=4))
