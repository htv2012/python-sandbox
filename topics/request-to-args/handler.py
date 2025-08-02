from dataclasses import dataclass


@dataclass(frozen=True)
class CommandRequest:
    global_kwargs: dict
    command_id: str
    command_kwargs: dict


def to_args(kwargs):
    for name, value in kwargs.items():
        yield f"--{name.replace('_', '-')}"
        if isinstance(value, list):
            yield from value
        elif value != "":
            yield value


def build_command(command: str, req: CommandRequest):
    args = [command]
    args.extend(to_args(req.global_kwargs))
    args.append(req.command_id)
    args.extend(to_args(req.command_kwargs))
    return args
