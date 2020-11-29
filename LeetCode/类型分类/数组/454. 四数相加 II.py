# 暴力
def fourSumCount(A, B, C, D):
    ans = 0
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    if a+b+c+d == 0:
                        ans+=1

    return ans

import collections
def fourSumCount2(A, B, C, D):
    countAB = collections.Counter(u + v for u in A for v in B)
    countCD = collections.Counter(u + v for u in C for v in D)
    ans = 0
    for x in countAB:
        for y in countCD:
            if x+y==0:
                ans += countAB[x]*countCD[y]
    return ans

def fourSumCount3(A, B, C, D):
    countAB = collections.Counter(u + v for u in A for v in B)
    ans = 0
    for u in C:
        for v in D:
            if -u - v in countAB:
                print(u,v,countAB[-u - v])
                ans += countAB[-u - v]
    return ans


A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
ans = fourSumCount3(A, B, C, D)
print(ans)