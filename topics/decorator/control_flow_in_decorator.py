print('Before definition')
def my_decorator(func):
    print('Invoke my_decorator for ', func)
    def innerExecutor():
        print("------------------------")
        func()
        print("------------------------")
    return innerExecutor
print('After definition')

@my_decorator
def func1():
    print('func1')

@my_decorator
def func2():
    print('func2')

func1()
func2()

