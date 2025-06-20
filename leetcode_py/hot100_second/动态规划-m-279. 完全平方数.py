"""
279. 完全平方数
已解答
中等
相关标签
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

"""

from utils import *
import math

'''
n=1, s=1, a=1
n=2, s=1+1, a=2
n=3, s=1+1+1, a=3
n=4, s=2, a=1
'''


class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化 全 1  的 dp
        dp = list(range(n + 1))
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                # print(i, j, j**2)
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)

                # print(i)

        # print(dp)

        return dp[-1]


if __name__ == '__main__':
    solve_batch(
        Solution, [
            (4, 1),
            (12, 3),
            # (13, 2),
        ]
    )
