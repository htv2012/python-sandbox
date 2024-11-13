import contextlib


class State:
    def __init__(self, sid, table, is_end: bool = False):
        self.sid = sid
        self.table = table
        self.is_end = is_end

    def __repr__(self):
        return f"({self.sid})"

    def next(self, state_input):
        with contextlib.suppress(KeyError):
            return self.table[state_input]
        return None


class Machine:
    def __init__(self):
        self.states = {}
        self.initial = 0
        # self.ids = itertools.count()
        # self.initial = next(self.ids)
        # self.current = self.initial

    def __repr__(self):
        return f"<{self.states}>"

    def add(self, sid, table, is_end: bool = False):
        self.states[sid] = State(sid, table, is_end)

    def solve(self, input_str):
        state = self.initial
        for input_ch in input_str:
            state = self.states[state].next(input_ch)
            if state is None:
                state = self.initial
            elif self.states[state].is_end:
                return True
        return self.states[state].is_end


# t = {}
# s0 = State(
#     0,
#     {
#         "a": 1,
#     },
# )
# t[s0.sid] = s0

# s1 = State(
#     1,
#     {
#         "b": 2,
#     },
# )
# t[s1.sid] = s1

# s2 = State(
#     2,
#     {
#         "c": 3,
#     },
#     is_end=True,
# )
# t[s2.sid] = s2
