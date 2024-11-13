class TestCase:
    pass

class MyTest(TestCase):
    def __init__(self):
        self.name = 'mytest'
        self.host = 'myhost'
        self.port = 8000

    def __getstate__(self):
        return {
            'name': self.name,
            'host': self.host,
            'port': self.port,
        }

    def __setstate__(self, state):
        self.name = state.get('name', self.name)
        self.host = state.get('host', self.host)
        self.port = state.get('port', self.port)
