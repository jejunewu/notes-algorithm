def backspaceCompare(S, T) -> bool:
    s1, s2= [], []
    for i in S:
        if i == '#' and s1:
            s1.pop()
        elif i != '#':
            s1.append(i)

    for i in T:
        if i == '#' and s2:
            s2.pop()
        elif i != '#':
            s2.append(i)
    return s1==s2

