"""

200. 岛屿数量
中等
2.3K
相关企业
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

"""

from typing import List


class Solution:
    def dfs(self, grid, i, j):
        """1的时候进入，按四个方向搜索改成0"""
        grid[i][j] = "0"
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x, y in directions:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == "1":
                self.dfs(grid, new_i, new_j)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)

        return count


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        cases=[
            ([
                 ["1", "1", "0", "0", "0"],
                 ["1", "1", "0", "0", "0"],
                 ["0", "0", "1", "0", "0"],
                 ["0", "0", "0", "1", "1"]
             ], 3),
        ]
    )
