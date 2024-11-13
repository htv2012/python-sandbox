#!/usr/bin/env python3
"""
main.py
Spawn 2 different apps, send input to them and receiving output.
https://stackoverflow.com/a/78789041/459745
"""

import pexpect

PROMPT = "> "


def main():
    """App Entry"""
    app1 = pexpect.spawn("python3 app1.py", echo=False, encoding="utf-8")
    app2 = pexpect.spawn("python3 app2.py", echo=False, encoding="utf-8")

    text_input = [
        "The more you learn",
        "I love my dog",
    ]

    for text in text_input:
        app1.expect(PROMPT)
        app1.sendline(text)
        output = app1.readline()
        output = output.rstrip()  # Convert bytes to str
        print(f"{text} -> {output} ", end="")

        app2.expect(PROMPT)
        app2.sendline(output)
        output2 = app2.readline()
        output2 = output2.rstrip()  # Convert bytes to str
        print(f"-> {output2}")

    # Quit apps
    app1.expect(PROMPT)
    app1.sendline("q")

    app2.expect(PROMPT)
    app2.sendline("q")


if __name__ == "__main__":
    main()
