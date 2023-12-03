"""

279. 完全平方数
中等
1.9K
相关企业
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9

提示：

1 <= n <= 104
通过次数
456.6K
提交次数
687.8K
通过率
66.4%

"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        分析：1. n内的最大平方数肯定在 int[sqrt(n)] 内
            2. dp减去最大平方数+1做比较

        """
        dp = list(range(n + 1))
        for i in range(2, n + 1):
            for j in range(1, int(n ** (1 / 2)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            (12, 3)
        ]
    )
