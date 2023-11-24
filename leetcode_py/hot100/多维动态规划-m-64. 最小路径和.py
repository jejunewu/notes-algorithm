"""

64. 最小路径和
中等
1.6K
相关企业
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

"""

from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]] * n] * m
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
            ([[1, 2, 3], [4, 5, 6]], 12)
        ]
    )
