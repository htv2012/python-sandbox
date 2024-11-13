# Else clause in exception means no except occurred

x = "no exception"

try:
    print(x)
except KeyError:
    print('Key error')
except NameError:
    print('Variable x not found')
else:
    print('else means no exception, not "other exception"')
