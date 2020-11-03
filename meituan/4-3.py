T = 1
N = 4#int(input())
A = [3,-2, 4,-1]#[int(i) for i in input().split()]

MAX = 0

dp = [0]*N
dp[0] = A[0]
idx = 0
for i in range(1, N):
    dp[i] += max(dp[i-1]+A[i], A[i])
if max(dp) > MAX:
    MAX = max(dp)
print(MAX)