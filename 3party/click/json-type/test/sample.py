import dataclasses
import enum


class SampleEnum(enum.Enum):
    """A SampleEnum enum for testing."""

    ONE = 1

    @classmethod
    def from_json(cls, json_object):
        name = json_object.upper()
        return cls[name]


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    is_admin: bool = False

    @classmethod
    def from_json(cls, json_object):
        uid = json_object["uid"]
        alias = json_object["alias"]
        is_admin = json_object.get("is_admin", False)
        assert isinstance(uid, int)
        assert isinstance(is_admin, bool)

        return cls(uid, alias, is_admin)


@dataclasses.dataclass
class ComplexDataClass:
    cid: int
    name: str
    sample: SampleEnum
    user: User

    @classmethod
    def from_json(cls, json_object):
        cid = json_object["cid"]
        name = json_object["name"]
        assert isinstance(cid, int)

        sample = SampleEnum.from_json(json_object["sample"])
        user = User.from_json(json_object["user"])

        return cls(cid, name, sample, user)
