# 只考虑'.'
def isMatch1(s: str, p: str) -> bool:
    if not p:
        return not s
    first_match = s and p[0] in {s[0], '.'}

    return first_match and isMatch1(s[1:], p[1:])


def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    # 第一个字母是否匹配
    first_match = bool(s and p[0] in {s[0],'.'})
    # 如果 p 第二个字母是 *
    if len(p) >= 2 and p[1] == "*":
        return isMatch(s, p[2:]) or first_match and isMatch(s[1:], p)
    else:
        return first_match and isMatch(s[1:], p[1:])


################### Test ########################
s,p = 'aaa', 'a.a'
ans1 = isMatch(s,p)
print(ans1)