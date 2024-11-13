import atexit


def hello(name):
    print(f'Hello, {name}')

def bye(name):
    print(f'Bye, {name}')


atexit.register(bye, 'world')


class Greeting:
    def __init__(self, name):
        self.name = name
        self.greet_count = 0

    def greet(self):
        self.greet_count += 1
        print(f'Greetings, {self.name} ({self.greet_count})')
        atexit.register(self.farewell)

    def farewell(self):
        print(f'Farewell, {self.name} ({self.greet_count})')
        self.greet_count -= 1
