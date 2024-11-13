# enclosure.py

def enc():
    counter = 0
    def do_something():
        counter += 1
        print('do something {}'.format(counter))

    return do_something

doit = enc()

doit()