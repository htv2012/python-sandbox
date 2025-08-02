from dataclasses import dataclass


@dataclass(frozen=True)
class CommandRequest:
    global_kwargs: dict
    command_id: str
    command_kwargs: dict


def to_args(kwargs):
    args = []
    for name, value in kwargs.items():
        args.append(f"--{name.replace('_', '-')}")
        if isinstance(value, list):
            args.extend(value)
        elif value != "":
            args.append(value)
    return args


def build_command(command: str, req: CommandRequest):
    args = [command]
    args.extend(to_args(req.global_kwargs))
    args.append(req.command_id)
    args.extend(to_args(req.command_kwargs))
    return args
