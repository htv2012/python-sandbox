from state import StatePersistence


class User(StatePersistence):
    keys = ['uid', 'alias', 'shell']

    def __init__(self, uid, alias, shell):
        self.uid = uid
        self.alias = alias
        self.shell = shell

    def __repr__(self):
        return 'User({0.uid!r}, {0.alias!r}, {0.shell!r})'.format(self)


if __name__ == '__main__':
    user = User(501, 'haiv', 'bash')
    print(user)
    print(user.__getstate__())

    # Set the atributes
    user.__setstate__({'shell': 'zsh', 'foo': 'bar'})
    print(user)
    print(user.__getstate__())
    print(user.__dict__)

