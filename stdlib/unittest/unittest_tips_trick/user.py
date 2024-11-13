class User(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __eq__(self, other):
        return self.name == other.name and self.uid == other.uid

    def __repr__(self):
        return 'User({!r}, {!r})'.format(self.name, self.uid)

    def __str__(self):
        return '{}({})'.format(self.name, self.uid)
