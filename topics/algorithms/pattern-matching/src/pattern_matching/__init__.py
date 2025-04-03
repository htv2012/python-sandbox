def jump_table(pattern: str):
    pattern = pattern
    table = {}
    pat_len = len(pattern)

    for index, ch in enumerate(pattern):
        table[ch] = pat_len - 1 - index
    del table[pattern[-1]]

    def calculate_jump(ch: str) -> int:
        nonlocal pat_len
        nonlocal table
        return table.get(ch, pat_len)

    return calculate_jump


def match(src: str, pat: str) -> int:
    """
    Boyer-Moore string matching algorithm
    https://youtu.be/4Oj_ESzSNCk?si=JEmgLMcNkx5fjrm-
    """
    if pat == "":
        raise ValueError("Pattern cannot be empty")

    jump = jump_table(pat)
    found_index = 0
    pat_len = len(pat)
    src_len = len(src)

    while (last_mismatch_index := found_index + pat_len - 1) < src_len:
        for index in reversed(range(pat_len)):
            if src[found_index + index] != pat[index]:
                found_index += jump(src[last_mismatch_index])
                break
        else:
            return found_index
    raise ValueError(f"Pattern not found: {pat}")
