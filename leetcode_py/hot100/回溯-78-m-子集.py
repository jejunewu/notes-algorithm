"""

78. 子集
中等
2.2K
相关企业
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

"""

from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def sub_arr(start_idx, arr):
            res.append(arr)
            for i in range(start_idx, n):
                sub_arr(i + 1, arr + [nums[i]])
        sub_arr(0, [])
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ]
    )
