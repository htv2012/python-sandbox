#!/usr/bin/env python3
import signal


def handler(signal_number, frame):
    print("\nsignal_number:", signal_number)
    print("frame:", frame)

    if frame is not None:
        print("back:", frame.f_back)
    print("Ctrl+C detected")
    raise SystemExit(1)


def main():
    signal.signal(signal.SIGINT, handler)
    age = input("Enter age (Ctrl+C to break out):")
    age = int(age)
    print(f"Your age: {age}")


if __name__ == "__main__":
    main()
