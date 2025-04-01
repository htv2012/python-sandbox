"""Explore class' property and attribute"""


class User(object):
    def __init__(self, uid, alias, shell="bash"):
        self.uid = uid
        self.alias = alias
        self.shell = shell
        print(locals())

    @property
    def shell_description(self):
        descriptions = dict(bash="Born-again shell")
        return descriptions[self.shell]


def main():
    u1 = User(501, "hai")
    print(u1.shell_description)
    print(getattr(u1, "shell_description"))


if __name__ == "__main__":
    main()
