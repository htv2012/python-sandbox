""""An equivalent to tail -f command for Python"""
import sys
import time


def tailf(path):
    last_position_read = 0
    while True:
        with open(path, "r") as stream:
            # Seek to where we left off
            stream.seek(last_position_read)
            
            for line in stream:
                yield line

            # Mark the position for the next time
            last_position_read = stream.tell()
        time.sleep(0.5)


def main():
    path = sys.argv[1]
    for line in tailf(path):
        line = line.strip()
        print(line)


if __name__ == "__main__":
    main()
