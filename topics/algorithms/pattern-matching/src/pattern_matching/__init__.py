def match(src, pat):
    if pat == "":
        raise ValueError()

    pat_len = len(pat)
    src_len = len(src)
    table = {}
    for index, ch in enumerate(pat):
        table[ch] = pat_len - 1 - index
    del table[ch]

    found = 0
    while (last := found + pat_len - 1) < src_len:
        for index in range(pat_len - 1, -1, -1):
            if src[found + index] != pat[index]:
                found += table.get(src[last], pat_len)
                break
        else:
            return found
    raise ValueError()
