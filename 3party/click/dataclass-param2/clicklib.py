import contextlib
import dataclasses
import enum
import functools
from typing import Optional

import click

__all__ = ["dataclass_options"]


def create_option(prefix, field):
    """Create a click option from a data class field."""
    decl = f"--{prefix}-{field.name.replace('_', '-')}"
    kwargs = {}

    if field.default_factory in {list, set}:
        kwargs["multiple"] = True
        # (first arg to List[str] or Set[str], which is str)
        kwargs["type"] = field.type.__args__[0]
    elif field.type is bool:
        kwargs["is_flag"] = True
        decl = f"{decl}/--no-{decl.removeprefix('--')}"
    elif issubclass(field.type, enum.Enum):
        kwargs["type"] = click.Choice(list(field.type.__members__))
    else:
        kwargs["type"] = field.type

    if (
        field.default is dataclasses.MISSING
        and field.default_factory is dataclasses.MISSING
    ):
        kwargs["required"] = True
    elif field.default is not dataclasses.MISSING:
        kwargs["default"] = field.default
        kwargs["show_default"] = True

    return click.option(decl, **kwargs)


def convert(value, default_factory, cls):
    """
    Convert a value.

    Args:
        value: The value to be converted, if None, no conversion performed.
        default_factory: The field default factory
    """
    if value is None:
        return value
    with contextlib.suppress(TypeError):
        # issubclass might generate a TypeError
        if issubclass(cls, enum.Enum):
            return cls[value]
    if default_factory is not dataclasses.MISSING:
        return default_factory(value)
    return value


def dataclass_options(cls, name: Optional[str] = None):
    """
    Create options to instantiate and object of type cls.

    Args:
        cls: The class
        name: The name to be passed into the decorated function.
            This name is also the prefix --<name>- to all options.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal func, cls, options, name, casts

            attrs = {}
            for field, cast in zip(dataclasses.fields(cls), casts):
                attrs[field.name] = kwargs.pop(f"{name}_{field.name}")
                attrs[field.name] = convert(attrs[field.name], cast, field.type)

            obj = cls(**attrs)
            kwargs[name] = obj

            return func(*args, **kwargs)

        nonlocal cls, name

        if name is None:
            name = cls.__name__.lower()
        options = [create_option(name, f) for f in dataclasses.fields(cls)]
        casts = [f.default_factory for f in dataclasses.fields(cls)]
        for opt in options:
            wrapped = opt(wrapped)

        return wrapped

    return decorator
