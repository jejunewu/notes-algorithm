def sortString(s: str) -> str:

    # 删除多余字符串
    def subStr(s, l):
        for i in l:
            s = s.replace(i, '', 1)
        return s

    ans,idx = '', 0
    while len(s)>0:
        if idx&1==0:
            tmp = sorted(set(s))
        else:
            tmp = sorted(set(s))[::-1]
        for i in tmp:
            ans+=i
        idx+=1
        s = subStr(s,tmp)
    return ans

s = "spo"
ans = sortString(s)
print(ans)