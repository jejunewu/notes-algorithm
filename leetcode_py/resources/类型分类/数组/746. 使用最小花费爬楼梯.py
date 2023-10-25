def minCostClimbingStairs(cost):
    size = len(cost)
    dp = [0]*(size)
    dp[1] = min(cost[0], cost[1])

    for i in range(2,size):
        dp[i] = min(dp[i-2]+cost[i-1], dp[i-1]+cost[i])
    return dp[-1]

cost = [10, 15, 20]
ans = minCostClimbingStairs(cost)
print(ans)