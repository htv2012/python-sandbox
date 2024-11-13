#
# Unintentional
#


def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))
print(append_to(2))


#
# Intentional
#

def fibbonacci(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fibbonacci(n - 1) + fibbonacci(n - 2)

    print('dbg<cache={}>'.format(cache))
    return cache[n]

print('\nFibbonacci numbers:')
for i in range(10):
    print(i, fibbonacci(i))
