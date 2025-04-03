from loguru import logger


def jump_table(pattern: str):
    pattern = pattern
    table = {}
    longest = len(pattern)

    for index, ch in enumerate(pattern):
        table[ch] = longest - 1 - index
    del table[pattern[-1]]

    def calculate_jump(ch: str) -> int:
        nonlocal longest
        nonlocal table
        return table.get(ch, longest)

    return calculate_jump


def match(src: str, pat: str) -> int:
    if pat == "":
        raise ValueError("Pattern cannot be empty")

    jump = jump_table(pat)
    found_index = 0
    longest = len(pat)

    while found_index < len(src):
        bad = src[found_index + longest - 1]
        logger.debug(f"{found_index=}, {bad=}")
        for index in reversed(range(longest)):
            if src[found_index + index] != pat[index]:
                logger.debug(
                    f"mismatched at {src[found_index + index]=} and {pat[index]=}"
                )
                skip = jump(bad)
                logger.debug(f"{skip=}")
                found_index += skip
                logger.debug(f"{found_index=}")
                break
        else:
            return found_index
    raise ValueError()
