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


def match(src: str, pat: str) -> index:
    jump = jump_table(pat)
    found_index = 0
    longest = len(pat)

    while found_index < len(src):
        bad = src[found_index + longest]
        logger.debug(f'{found_index=}, {bad=}')
        for index in reversed(range(longest)):
            if src[found_index + index] != pat[index]:
                logger.debug(f'mismatched at {src


