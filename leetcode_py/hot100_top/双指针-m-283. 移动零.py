"""
283. 移动零
已解答
简单
相关标签
相关企业
提示
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


"""
from utils import *

"""
i: 快指针
j: 慢指针 
一次循环即可
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1

        return nums


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0])
        ]

    )
