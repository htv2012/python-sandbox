import select
import sys


def timed_input(prompt, default, timeout: int = 10, show_default: bool = True):
    sys.stdout.write(prompt)
    if show_default:
        sys.stdout.write(f"[{default}] ")
    sys.stdout.flush()
    stdin_list, _, _ = select.select([sys.stdin], [], [], timeout)

    if stdin_list:
        answer = stdin_list[0].readline().rstrip()
    else:
        print()
        answer = default
    return answer or default


name = timed_input("What is your name? ", default="stranger", timeout=5)
print(f"Hello, {name}")
