a = '3332'
# a=a[:-1]
# print(a)
print(a[0] < a[1])

def check(s,cnt):
    if len(s) <=1 or s[-2]<=s[-1]:
        print(s,cnt)
        return s+'9'*cnt
    else:
        cnt+=1
        check(s[:-1], cnt)



ans = check(a,0)
print(ans)
