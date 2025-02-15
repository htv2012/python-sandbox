import pathlib
import time

import tqdm


def main():
    """Simulate reading a very large file in chunks of N bytes at a time."""
    file = pathlib.Path(__file__)
    size = file.stat().st_size
    chunk_size = 10

    with tqdm.tqdm(total=size) as pbar:
        while size > 0:
            time.sleep(0.3)
            pbar.update(chunk_size)
            size -= chunk_size


if __name__ == "__main__":
    main()
