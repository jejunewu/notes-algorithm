"""
322. 零钱兑换
已解答
中等
相关标签
相关企业
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

from utils import *

'''
[1, 2, 5]

dp[0] = 0
dp[1] = 1
dp[2] = min()

状态转移方程：dp[i] = min(dp[i], dp[i-coin] + 1)


'''


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


if __name__ == '__main__':
    solve_batch(
        Solution, [
            ([1, 2, 5], 11, 3),
            # (13, 2),
        ]
    )
