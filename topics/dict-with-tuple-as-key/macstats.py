import dataclasses


@dataclasses.dataclass(frozen=True)
class Telemetry:
    namespace: str
    telemetry_id: str


class MacStats(dict):
    def __init__(self, mac2: bool):
        self.mac2 = mac2

    def contain_lru(self, key):
        print(f">>> Check contain: {key!r}")
        return any(key == k[0] for k in self)

m = MacStats(True)
t1 = Telemetry("ns1", "id1")
m[t1, "num-1", "name1"] = 100
print(m)
print(f"{m.contain_lru(t1)=}")

