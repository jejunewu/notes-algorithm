"""
215. 数组中的第K个最大元素
中等
2.3K
相关企业
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

"""
from typing import List


class Solution:
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        """内置方法，笔试无用"""
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """快排"""
        # TODO
        return 0


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]
    solve_batch(Solution, cases)
