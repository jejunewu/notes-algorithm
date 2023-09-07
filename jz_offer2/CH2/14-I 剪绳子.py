def cuttingRope(n):
    dp = [0,1,1] + [0]*(n-2)
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
    return dp[n]



################### Test ########################
n = 8
ans = cuttingRope(n)
print(ans)