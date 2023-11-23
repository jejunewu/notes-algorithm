"""
994. 腐烂的橘子
中等
778
相关企业
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。



示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2

"""
from typing import *
import copy


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def rotting_minute():
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            ref = copy.deepcopy(grid)
            count_1 = 0
            for i in range(m):
                for j in range(n):
                    if ref[i][j] == 2:
                        for x, y in directions:
                            new_i = i + x
                            new_j = j + y
                            if 0 <= new_i < m and \
                                    0 <= new_j < n and \
                                    grid[new_i][new_j] == 1:
                                grid[new_i][new_j] = 2
                    elif ref[i][j] == 1:
                        count_1 += 1
            return ref != grid, count_1

        minutes = 0
        flag = True
        count_1 = 0
        while flag:
            flag, count_1 = rotting_minute()
            minutes += 1
        if count_1:
            return -1
        return minutes - 1


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
            ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
            ([[0, 2]], 0)
        ]
    )
