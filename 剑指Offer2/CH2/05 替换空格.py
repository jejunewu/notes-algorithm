def replaceSpace(s: str) -> str:
    spaceN = 0
    size = len(s)
    for i in s:
        if i == ' ':
            spaceN+=1
    s = s+'0'*(spaceN*2)

    p1,p2 = size-1, size+(spaceN*2)-1
    while p1>=0 and p1 != p2:
        if s[p1] == ' ':
            s = s[:p2-2] + '%20' + s[p2+1:]
            p1-=1
            p2 = p2-3
        else:
            s = s[:p2]+s[p1]+s[p2+1:]
            p1-=1
            p2-=1

    return s

################### Test ########################
s = "We are happy."
ans = "We%20are%20happy."

res = replaceSpace(s)
print(res)