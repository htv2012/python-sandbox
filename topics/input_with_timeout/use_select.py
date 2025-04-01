import select
import sys

print("What is your name? ", end="")
sys.stdout.flush()
i, o, e = select.select([sys.stdin], [], [], 10)

if i:
    name = sys.stdin.readline().strip()
else:
    name = "stranger"

print(f"Hello, {name}")
