#!/usr/bin/env python3
import dataclasses


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: str

    def __format__(self, spec):
        """Spec: u: uid, a: alias, s: shell"""
        if spec == "":
            spec = "a"
        if len(spec) == 1:
            width = ""
        else:
            width, spec = spec[:-1], spec[-1]

        if spec == "a":
            value = self.alias
        elif spec == "u":
            value = self.uid
        elif spec == "s":
            value = self.shell
        else:
            raise ValueError(f"Invalid format spec: {spec!r}")

        out = f"{value:{width}}"
        return out


def main():
    user = User(uid=501, alias="karen", shell="bash")
    print("repr:", repr(user))
    print("-" * 20)

    print(f"Spec=u: {user:>12u}")  # Right justify
    print(f"Spec=a: {user:12a}")  # Left justify
    print(f"Spec=:  {user}")  # No spec
    print(f"Spec=s: {user:^12s}")  # Center


if __name__ == "__main__":
    main()
