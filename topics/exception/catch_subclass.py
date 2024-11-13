class NameTooShort(ValueError):
    pass

def validate(name):
    if len(name) < 2:
        raise NameTooShort(name)
    if len(name) > 20:
        raise ValueError('Name is too long: {}'.format(name))
    print('Name {!r} is OK'.format(name))


validate('Joe')
try:
    validate('E')

except NameTooShort as e:
    # Need to catch this before catching ValueError
    print('Name too short:', e)
except ValueError as e:
    print('Value Error:', e)
