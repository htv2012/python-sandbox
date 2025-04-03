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
