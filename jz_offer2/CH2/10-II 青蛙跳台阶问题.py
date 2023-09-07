def numWays(n: int) -> int:
    if n == 0 or n==1:
        return 1
    elif n == 2:
        return 2
    else:
        idx = 3
        pre, post = 1, 2
        while idx <= n:
            tmp = post
            post += pre
            pre = tmp
            idx += 1
        return post % 1000000007


################### Test ########################
ans = numWays(20)
print(ans)