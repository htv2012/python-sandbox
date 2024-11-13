def object_factory(raw):
    if isinstance(raw, (list, dict)):
        return JsonObject(raw)
    else:
        return raw


class JsonObject:
    def __init__(self, raw):
        self.raw = raw

    def __getitem__(self, key):
        return self.raw[key]

    def __setitem__(self, key, value):
        keys = key.split(".")
        last = keys.pop(-1)
        node = self.raw
        for key in keys:
            node = node.setdefault(key, {})
        node[last] = value


j = JsonObject({"foo": "bar"})
print(j["foo"])
