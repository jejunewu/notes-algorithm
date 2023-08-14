def firstUniqChar(s: str) -> int:

    for i in range(len(s)):
        if s[i] not in s[:i]+s[i+1:]:
            return i
    return -1

s = "ab"
ans = firstUniqChar(s)
print(ans)