import dataclasses

from class_serializer import serialize_object


@dataclasses.dataclass
class Command:
    uid: int
    command: str
    code: int
    result: str


@serialize_object.register(Command)
def serialize_command(obj: Command):
    return {
        "___class__": "Command",
        "uid": obj.uid,
        "command": obj.command,
        "code": obj.code,
        "result": obj.result,
    }
