import collections
import collections.abc

Transaction = collections.namedtuple("Transaction", "op, index, value, prev_value")


class TrackableList(collections.abc.MutableSequence):
    def __init__(self, seq=None):
        self.data = list(seq or [])
        self.transactions = []

    def _record(self, op, index, value, prev_value):
        self.transactions.append(Transaction(op, index, value, prev_value))

    def __getitem__(self, index):
        value = self.data[index]
        self._record("get", index, value, None)
        return value

    def __setitem__(self, index, value):
        prev_value = self.data[index]
        self.data[index] = value
        self._record("set", index, value, prev_value)

    def __delitem__(self, index):
        prev_value = self.data[index]
        del self.data[index]
        self._record("delete", index, None, prev_value)

    def __len__(self):
        return len(self.data)

    def insert(self, index, value):
        self.data.insert(index, value)
        self._record("insert", index, value, None)
