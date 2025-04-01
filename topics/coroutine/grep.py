from coroutine import coroutine


@coroutine
def grep(pattern):
    print("Looking for %r" % pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)
