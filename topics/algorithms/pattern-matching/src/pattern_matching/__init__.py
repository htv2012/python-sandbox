def match(src: str, pat: str) -> int:
    """
    Boyer-Moore string matching algorithm
    https://youtu.be/4Oj_ESzSNCk?si=JEmgLMcNkx5fjrm-
    """
    if pat == "":
        raise ValueError("Pattern cannot be empty")

    # Create bad jump table
    pat_len = len(pat)
    src_len = len(src)
    table = {}
    for index, ch in enumerate(pat):
        table[ch] = pat_len - index - 1
    del table[ch]

    # Scan/compre from right to left
    found_index = 0
    while (last_mismatch_index := found_index + pat_len - 1) < src_len:
        for index in range(pat_len - 1, -1, -1):
            if src[found_index + index] != pat[index]:
                found_index += table.get(src[last_mismatch_index], pat_len)
                break
        else:
            return found_index
    raise ValueError(f"Pattern not found: {pat}")
