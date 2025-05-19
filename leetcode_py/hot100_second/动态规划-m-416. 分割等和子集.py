"""
416. 分割等和子集
已解答
中等
相关标签
相关企业
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import *

'''
1. 判断是否为偶数，若为奇数，则返回 False

2. 定义状态转移空间 (m+1) * (n+1) 

3. 定义状态转移方程
    1) f[i-1][j]
    2) j>=x & f[i-1][j-x]

'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m, mod = divmod(sum(nums), 2)
        if mod:
            return False

        n = len(nums)

        # 定义 (m+1) * (n+1) 的状态转移空间
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True

        for i, x in enumerate(nums, 1):
            for j in range(m + 1):
                # 条件1：如果 f[i-1][j] 为 True，即前 i-1 个元素中已有子集和为 j，那么无需选取 x，也可以得到 j，所以 f[i][j] = True
                # 条件2：如果 j >= x，并且 f[i-1][j-x] 为 True，即前 i-1 个元素中已有子集和为 j-x，那么选取 x，也可以得到 j，所以 f[i][j] = True
                f[i][j] = f[i - 1][j] or (j >= x and f[i - 1][j - x])

        return f[n][m]


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([1, 5, 11, 5], True),
            # ([1, 2, 3, 5], False)
        ]

    )
