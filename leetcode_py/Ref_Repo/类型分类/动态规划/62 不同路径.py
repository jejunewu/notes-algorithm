def uniquePaths(m: int, n: int):
    dp = [[0]*(n+1)]*(m+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = max(1, (dp[i-1][j] + dp[i][j-1]))

    return dp[-1][-1]

m,n = 3,2
ans = uniquePaths(m,n)
print(ans)