"""

54. 螺旋矩阵
提示
中等
1.5K
相关企业
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



示例 1：


输入：matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

from typing import *

"""
矩阵按方向遍历
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            # →
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b: break

            # ↓
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l: break

            # ←
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t: break

            # ↑
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
        ]
    )
