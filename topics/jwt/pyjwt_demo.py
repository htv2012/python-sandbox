#!/usr/bin/env python3
"""
A Python skeleton script
"""

import jwt


def main():
    """Entry"""

    key = "fiFiFoFumBananaRamaPooPooKaka"
    raw = (
        b"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        b"eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I"
        b"kpvaG4gQ2FycGVudGVycyIsImlhdCI6MTUxNj"
        b"IzOTAyMn0.Gos9Vh_5nh_Q7opHCjX1TubnNju"
        b"ixeStGafFSwNP-yc"
    )
    header = jwt.get_unverified_header(raw)
    algorithm = header["alg"]
    payload = jwt.decode(raw, key=key, algorithms=algorithm)

    print(f"{header=}")
    print(f"{payload=}")


if __name__ == "__main__":
    main()
