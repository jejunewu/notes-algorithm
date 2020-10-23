def myPow(x: float, n: int):

    if x == 0:
        return 0

    res = 1
    if n < 0:
        x, n = 1 / x, -n

    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


################### Test ########################
ans = myPow(2,10)
print(ans)