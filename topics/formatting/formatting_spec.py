#!/usr/bin/env python3
import dataclasses
import os
import re



SPEC_PATTERN = re.compile(
    r"""
    ^             # Start
    ([<>^])?      # One of: < > or ^
    (\d*)?        # The width, a series of digits
    (alias|shell|uid|csv)?
    $             # End
""",
    re.VERBOSE,
)


def parse_spec(spec: str):
    matched = SPEC_PATTERN.match(spec)
    alignment, width, selector = matched.groups()
    return alignment or "", width or "", selector or ""


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: str

    def __format__(self, spec):
        """Spec: uid, alias, shell"""
        alignment, width, selector = parse_spec(spec)
        if selector == "alias" or selector == "":
            value = self.alias
        elif selector == "uid":
            value = self.uid
        elif selector == "shell":
            value = self.shell
        elif selector == "csv":
            value = f"{self.uid},{self.alias},{self.shell}"
        else:
            raise ValueError(f"Invalid format spec: {spec!r}")

        out = f"{value:{alignment}{width}}"
        return out


def main():
    user = User(uid=501, alias="karen", shell="bash")
    print(f"User = {user!r}")


    print("\n# No alignment")
    for spec in ["| {}| ", "| {:uid} |", "| {:alias} |", "| {:shell} |"]:
        print(spec.format(user))

    print("\n# Left Justify")
    for spec in ["| {:<12} |", "| {:<12uid} |", "| {:<12alias} |", "| {:<12shell} |"]:
        print(spec.format(user))

    print("\n# Right Justify")
    for spec in ["| {:>12} |", "| {:>12uid} |", "| {:>12alias} |", "| {:>12shell} |"]:
        print(spec.format(user))

    print("\n# Center")
    for spec in ["| {:^12} |", "| {:^12uid} |", "| {:^12alias} |", "| {:^12shell} |"]:
        print(spec.format(user))



if __name__ == "__main__":
    main()
