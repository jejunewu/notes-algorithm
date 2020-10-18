def movingCount(m: int, n: int, k: int):

    def sumInt(m, n):
        res = 0
        while m > 0 and n > 0:
            res += m % 10 + n % 10
            m //= 10
            n //= 10
        if m > 0 or n > 0:
            tmp = max(m, n)
            while tmp > 0:
                res += tmp % 10
                tmp //= 10
        return res

    res=0
    for i in range(m):
        for j in range(n):
            if sumInt(i,j) <= k:
                print(i,j)
                res+=1

    return res

################### Test ########################
m = 16
n = 8
k = 4

ans = movingCount(m,n,k)
print('abc: ',ans)





