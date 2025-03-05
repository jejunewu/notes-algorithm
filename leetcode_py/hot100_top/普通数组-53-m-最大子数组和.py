"""
53. 最大子数组和
中等
6.4K
相关企业
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List

"""

动态规划：
- 
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            res = max(res, nums[i])
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([5, 4, -1, 7, 8], 23),
        ([1], 1)
    ]

    solve_batch(
        Solution,
        cases,
    )
