"""
Use a crude finite state machine to parse the expression "N + M"
where N and M are two unsigned integers
"""


class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"State({self.name})"

    def __hash__(self):
        return hash(self.name)


class Machine:
    def __init__(self, initial_state):
        self.state = initial_state
        self.actions = {}
        self.next_state = {}

    def transition(self, current_state, stimulant, action, next_state):
        self.next_state[current_state, stimulant] = next_state
        self.actions[current_state, stimulant] = action

    def __repr__(self):
        return f"Machine(state={self.state})"

    def accept(self, input_value):
        try:
            next_state = self.next_state[self.state, input_value]
        except KeyError:
            raise ValueError(f"State {self.state} does not accept {input_value!r}")
        print(f"{self.state} + {input_value!r} ==> {next_state}")
        action = self.actions[self.state, input_value]
        if action is not None:
            action(input_value)
        self.state = next_state


def store_left(char_input):
    global left
    left += char_input


def store_right(char_input):
    global right
    right += char_input


left = ""
right = ""

initial = State("initial")
left_operand = State("left_operand")
blanks1 = State("blanks1")
operator = State("operator")
blanks2 = State("blanks2")
right_operand = State("right_operand")

machine = Machine(initial)

for char_input in "0123456789":
    machine.transition(
        initial, stimulant=char_input, action=store_left, next_state=left_operand
    )
    machine.transition(
        left_operand, stimulant=char_input, action=store_left, next_state=left_operand
    )
machine.transition(left_operand, stimulant="+", action=None, next_state=operator)

# Blanks1
machine.transition(left_operand, stimulant=" ", action=None, next_state=blanks1)
machine.transition(blanks1, stimulant=" ", action=None, next_state=blanks1)
machine.transition(blanks1, stimulant="+", action=None, next_state=operator)

# Blanks2
machine.transition(blanks2, stimulant=" ", action=None, next_state=blanks2)

# Operator
machine.transition(operator, stimulant=" ", action=None, next_state=blanks2)
for char_input in "0123456789":
    machine.transition(
        blanks2, stimulant=char_input, action=store_right, next_state=right_operand
    )
    machine.transition(
        operator, stimulant=char_input, action=store_right, next_state=right_operand
    )

# Right operand
for char_input in "0123456789":
    machine.transition(
        right_operand,
        stimulant=char_input,
        action=store_right,
        next_state=right_operand,
    )

# Crank the machine
for char_input in " 12  + 131":
    machine.accept(char_input)

print(f"left={left}")
print(f"right={right}")
