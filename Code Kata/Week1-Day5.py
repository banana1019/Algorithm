def get_prefix(strs):
    c = []
    for a in strs:
        for b in a:
            c.append(b)
    d = ''
    for i in c:
        if c.count(i) == len(c):
            d = strs[0]
        if c.count(i) >= len(strs) and i not in d:
            d = d + i
    return d
