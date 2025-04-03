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
        for index in reversed(range(longest)):
            if src[found_index + index] != pat[index]:
                skip = jump(bad)
                found_index += skip
                break
        else:
            return found_index
    raise ValueError()
