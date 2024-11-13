import argparse
import enum


def enum_choice_action(enum_class: enum.EnumType):
    """Return an Action class with choices from `enum_class`."""

    class EnumChoiceAction(argparse.Action):
        def __init__(
            self,
            option_strings,
            dest,
            nargs=None,
            const=None,
            default=None,
            type=None,
            choices=None,
            required=False,
            help=None,
            metavar=None,
        ):
            super().__init__(
                option_strings=option_strings,
                dest=dest,
                nargs=nargs,
                const=const,
                default=default,
                type=type,
                choices=choices or [member.name for member in enum_class],
                required=required,
                help=help,
                metavar=metavar,
            )
            self.enum_class = enum_class

        def __call__(
            self,
            parser: argparse.ArgumentParser,
            namespace: argparse.Namespace,
            values,
            option_string: str | None = None,
        ) -> None:
            setattr(namespace, self.dest, self.enum_class[values])

    return EnumChoiceAction
