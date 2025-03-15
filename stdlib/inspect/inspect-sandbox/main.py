import inspect
import io
import textwrap


class User:
    def __init__(self, uid, alias, shell):
        self.uid = uid
        self.alias = alias
        self.shell = shell

    def is_root(self) -> bool:
        """Return True if the user is root."""
        return self.uid == 0

    def is_admin(self) -> bool:
        """
        Return True if the user is an administrator.

        An administrator UID is 501.
        """
        return self.uid == 501


def explore(user):
    buffer = io.StringIO()
    print(f"\n# Explore {user.__class__.__name__} object")
    for name, value in inspect.getmembers(user):
        if name.startswith("__"):
            continue
        if callable(value):
            print(f"{name}{inspect.signature(value)}")
            if doc := inspect.getdoc(value):
                doc = textwrap.fill(doc, initial_indent="  ", subsequent_indent="  ")
                print(doc)
        else:
            buffer.write(f"{name} = {value!r}\n")
    if attributes := buffer.getvalue():
        print(attributes)


def main():
    user = User(501, "haiv", "zsh")
    explore(user)


if __name__ == "__main__":
    main()
