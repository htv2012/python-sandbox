import collections
import json
import os


class TestCase:
    def __init__(self):
        self.options = {}

    def __setstate__(self, state):
        self.options = state

        # For variable 'abort_session', the env var will overwrite the
        # state
        settings = collections.ChainMap(os.environ, state)
        envvar = settings.get("abort_session", "false")
        envvar = json.loads(envvar)
        self.options["abort_session"] = envvar

    def __getstate__(self):
        return self.options


if __name__ == "__main__":
    tc = TestCase()
    tc.__setstate__({"foo": "bar"})
    print(tc.options)
