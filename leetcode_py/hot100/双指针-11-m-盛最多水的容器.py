"""

11. 盛最多水的容器
提示
中等
4.7K
相关企业
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。



示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1


提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""

from typing import *

"""
双指针做
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * (min(height[r], height[l])))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([0, 0], 0),
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ]
    )
