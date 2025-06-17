#!/usr/bin/env python3
import dataclasses
import logging
import os
import re

logging.basicConfig(level=os.getenv("LOGLEVEL", "DEBUG"))
logger = logging.getLogger(__name__)


SPEC_PATTERN = re.compile(
    r"""
    ^             # Start
    ([<>^])?      # One of: < > or ^
    (\d*)?        # The width, a series of digits
    (a|s|u|csv)?  # a=alias, s=shell, u=uid, csv=comma separated values
    $             # End
""",
    re.VERBOSE,
)


def parse_spec(spec: str):
    logger.debug("spec=%r", spec)
    matched = SPEC_PATTERN.match(spec)
    logging.debug("matched=%r", matched)
    if matched:
        logging.debug("groups=%r", matched.groups())

    alignment, width, selector = matched.groups()
    return alignment or "", width or "", selector or ""


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: str

    def __format__(self, spec):
        """Spec: u: uid, a: alias, s: shell"""
        alignment, width, selector = parse_spec(spec)
        if selector == "a" or selector == "":
            value = self.alias
        elif selector == "u":
            value = self.uid
        elif selector == "s":
            value = self.shell
        elif selector == "csv":
            value = f"{self.uid},{self.alias},{self.shell}"
        else:
            raise ValueError(f"Invalid format spec: {spec!r}")

        out = f"{value:{alignment}{width}}"
        return out


def main():
    user = User(uid=501, alias="karen", shell="bash")
    print("repr:", repr(user))
    print("-" * 20)

    print("\n# No spec")
    print("123456789012")
    print(f"{user}")

    print("\n# Spec='>12u'")
    print("123456789012")
    print(f"{user:>12u}")

    print("\n# Spec='12a'")
    print("123456789012")
    print(f"{user:12a}")  # Left justify

    print("\n# Spec='^12s'")
    print("123456789012")
    print(f"{user:^12s}")  # Center

    print("\n# Spec='csv'")
    print(f"{user:csv}")


if __name__ == "__main__":
    main()
