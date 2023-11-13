"""
35. 搜索插入位置
简单
2.2K
相关企业
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。



示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4


提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104

"""

from typing import List


class Solution:
    """ 用二分查找方法 """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2  # 防止 l+r 溢出
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 7, 4),
        ]
    )
