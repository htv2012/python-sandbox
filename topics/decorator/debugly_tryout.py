""" Try out the debug decorator """


from debugly import debug


@debug
def greet(name, phrase=''):
    print('Hello, {}. {}'.format(name, phrase))

greet('world')
greet('John', phrase='How are you?')
