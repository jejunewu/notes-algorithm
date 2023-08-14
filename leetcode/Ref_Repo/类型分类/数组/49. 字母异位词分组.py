def groupAnagrams(strs):
    d = {}
    for s in strs:
        tmp = ''.join(sorted(s))
        if tmp in d:
            d[tmp].append(s)
        else:
            d[tmp] = [s]
    return list(d.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = groupAnagrams(strs)
print(ans)