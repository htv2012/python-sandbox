import importlib
import pathlib
import sys
import types

import click

__all__ = ["main"]
__version__ = "1.0.1"


class MyGroup(click.Group):
    """Group the sub commands

    - The file names will be command name, e.g. show_status.py -> show-status
    - In each file, the main function will be the sub command
    - File names which start with underscore will be ignore. They are mean for support.
    """

    def __init__(self, plugins_dir, **kwargs):
        super().__init__(**kwargs)
        self.plugins_dir = plugins_dir

    def list_commands(self, ctx: click.Context):
        commands = [
            path.stem.replace("_", "-")
            for path in self.plugins_dir.glob("*.py")
            if not path.stem.startswith("_")
        ]
        return sorted(commands)

    def get_command(self, ctx: click.Context, name):
        sys.path.insert(0, str(self.plugins_dir))
        try:
            mod_name = name.replace("-", "_")
            mod = importlib.import_module(mod_name)
            return mod.main
        except ModuleNotFoundError:
            ctx.fail(f"Cannot load command: {name}")
        finally:
            del sys.path[0]


PLUGINS_DIR = pathlib.Path(__file__).parent.parent / "plugins"


@click.command(cls=MyGroup, plugins_dir=PLUGINS_DIR)
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.version_option(version=__version__)
@click.pass_context
def main(ctx: click.Context, verbose):
    ctx.ensure_object(types.SimpleNamespace)
    ctx.obj.verbose = verbose
