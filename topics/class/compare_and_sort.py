class User(object):
    def __init__(self, uid, alias, browser):
        self.uid = uid
        self.alias = alias
        self.browser = browser

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"uid={self.uid!r}"
            f", "
            f"alias={self.alias!r}"
            f", "
            f"browser={self.browser!r}"
            f")"
        )

    # This is needed for equality comparison, not needed for sorting
    def __eq__(self, other):
        return self.uid == other.uid

    # In order to sort, implement this method
    def __lt__(self, other):
        return self.uid < other.uid


users = [
    User(508, "john", "Firefox"),
    User(501, "karen", "Chrome"),
]

print(sorted(users))
