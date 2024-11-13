#!/usr/bin/env python
def type_input(prompt, cast=str):
    try:
        ask = raw_input
    except NameError:
        ask = input

    while True:
        try:
            raw_value = ask(prompt)
            value = cast(raw_value)
            return value
        except (ValueError, TypeError) as e:
            pass


if __name__ == "__main__":
    uid = type_input("User ID: ", int)
    print("uid = %r" % uid)

    hex_value = type_input("Hex value: ", cast=lambda s: int(s, 16))
    print("hex_value = %r" % hex_value)
