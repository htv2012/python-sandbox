import enum
import functools
import pathlib

import yaml

__all__ = ["ConfigFile"]

CONFDIR = pathlib.Path(__file__).with_name("config").relative_to(pathlib.Path.cwd())
CONF_ALIASES = {
    "default": "Config1",
    "normal": "Config1",
}


class ConfigFile(enum.Enum):
    """A configuration file."""

    Config1 = "config1"
    Config2 = "config2"

    _aliases = {
        "default": "Config1",
        "normal": "Config1",
    }

    @functools.cached_property
    def path(self):
        """Path to the configuration file."""
        base_name = CONF_ALIASES.get(self.value, self.value)
        return CONFDIR / f"{base_name}.yaml"

    @functools.cached_property
    def content(self):
        """Content of the configuration file."""
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def names(cls):
        """Names of the members."""
        return [v.name for v in cls] + list(CONF_ALIASES)

    @classmethod
    def from_param(cls, ctx, param, value):
        """Callback to convert string value to member."""
        value = CONF_ALIASES.get(value, value)  # Look up alias
        return cls[value]
