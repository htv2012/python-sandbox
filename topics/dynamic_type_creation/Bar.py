class Bar(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        attrs = ', '.join('{}={!r}'.format(k, v) for k, v in list(self.__dict__.items()))
        return '{}({})'.format(self.__class__.__name__, attrs)
