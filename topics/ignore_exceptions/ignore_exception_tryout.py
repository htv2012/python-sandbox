
from ignore_exceptions import ignore_exceptions

with ignore_exceptions(ZeroDivisionError, AttributeError, IndexError):
    print('Before')
    [1,2,3][6]
    print('After')
print('Finally')
