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
    reverse_line = pexpect.spawn(
        "python3 reverse_line.py", echo=False, encoding="utf-8"
    )
    reverse_words = pexpect.spawn(
        "python3 reverse_words.py", echo=False, encoding="utf-8"
    )

    text_input = [
        "The more you learn",
        "I love my dog",
        "cấm không được vào",
    ]

    for text in text_input:
        reverse_line.expect(PROMPT)
        reverse_line.sendline(text)
        output = reverse_line.readline()
        output = output.rstrip()  # Convert bytes to str
        print(f"{text} -> {output} ", end="")

        reverse_words.expect(PROMPT)
        reverse_words.sendline(output)
        output2 = reverse_words.readline()
        output2 = output2.rstrip()  # Convert bytes to str
        print(f"-> {output2}")

    # Quit apps
    reverse_line.expect(PROMPT)
    reverse_line.sendline("q")

    reverse_words.expect(PROMPT)
    reverse_words.sendline("q")


if __name__ == "__main__":
    main()
