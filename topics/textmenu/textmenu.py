def menu(prompt, choices):
    print('\n\n{0}\n'.format(prompt))
    count = len(choices)
    for i, choice in enumerate(choices, 1):
        print('{0:>3}) {1}'.format(i, choice))

    while True:
        response = input('> ')
        if response in choices:
            return response
        try:
            number = int(response)
            if number > 0 and number <= count:
                return choices[number - 1]
        except ValueError:
            pass
