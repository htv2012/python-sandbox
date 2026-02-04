import dataclasses

import click


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    admin: bool = False
    security_score: float = 0.75
    groups: list[str] = dataclasses.field(default_factory=list)


for f in dataclasses.fields(User):
    for name in "name type default default_factory init repr".split():
        print(f"{name} = {getattr(f, name)}")
    print()


def create_option(prefix, field):
    kwargs = dict(type=field.type)
    if field.default is not dataclasses.MISSING:
        kwargs["default"] = field.default

    return click.option(f"--{prefix}-{field.name.replace('_', '-')}", **kwargs)


def options(cls):
    prefix = cls.__name__.lower()
    _options = [create_option(prefix, f) for f in dataclasses.fields(cls)]

    def pre_func(**kwargs):
        nonlocal cls, _options, prefix
        attrs = {}
        for field in dataclasses.fields(cls):
            attrs[field.name] = kwargs.pop(f"{prefix}_{field.name}")
        obj = cls(**attrs)
        kwargs[prefix] = obj
        print(f"{kwargs=}")


    def wrapped(func):
        nonlocal pre_func
        for opt in reversed(_options):
            pre_func = opt(pre_func)
        return pre_func

    return wrapped


@click.command
@options(User)
def main(uid, alias, admin, security_score, groups):
    print(f"{uid=}")
    print(f"{alias=}")
    print(f"{admin=}")
    print(f"{security_score=}")
    print(f"{groups=}")


if __name__ == "__main__":
    main()
