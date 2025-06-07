import importlib
import pathlib
import types

import click

__all__ = ["main"]
__version__ = "1.0.0"


class MyGroup(click.Group):
    """Group the sub commands

    - The file names will be command name, e.g. show_status.py -> show-status
    - In each file, the main function will be the sub command
    - File names which start with underscore will be ignore. They are mean for support.
    """

    def list_commands(self, ctx: click.Context):
        root = pathlib.Path(__file__).parent / "commands"
        commands = [
            path.stem.replace("_", "-")
            for path in root.glob("*.py")
            if not path.stem.startswith("_")
        ]
        return sorted(commands)

    def get_command(self, ctx: click.Context, name):
        try:
            mod_name = name.replace("-", "_")
            mod = importlib.import_module(f"dynamic_subcommands.commands.{mod_name}")
            return mod.main
        except ModuleNotFoundError:
            ctx.fail(f"Cannot load command: {name}")


@click.command(cls=MyGroup)
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.version_option(version=__version__)
@click.pass_context
def main(ctx: click.Context, verbose):
    ctx.ensure_object(types.SimpleNamespace)
    ctx.obj.verbose = verbose
