import dataclasses

from class_serializer import serialize_object


@dataclasses.dataclass
class User:
    uid: int
    alias: str


@serialize_object.register(User)
def serialize_user(obj: User):
    return {
        "__class__": "User",
        "uid": obj.uid,
        "alias": obj.alias,
    }
