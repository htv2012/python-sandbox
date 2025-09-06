import io


def roman(ara: int) -> str:
    lookup = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    buf = io.StringIO()
    for dividend, rom in lookup:
        count, ara = divmod(ara, dividend)
        buf.write(count * rom)
    return buf.getvalue()


def arabic(rom: str) -> int:
    lookup = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    out = 0
    last = None
    for ch in rom:
        if last is not None and lookup[ch] > lookup[last]:
            out -= lookup[last] * 2
        out += lookup[ch]
        last = ch
    return out
