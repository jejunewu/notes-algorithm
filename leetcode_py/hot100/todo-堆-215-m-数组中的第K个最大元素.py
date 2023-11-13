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


提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List

""" 堆方法 """

""" 快排 超时！ """


class Solution:

    def _partition(self, arr, low, high):
        pivot = arr[low]
        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= pivot:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        return low

    def _quick_sort(self, arr, low, high):
        if low >= high:
            return
        pivotpos = self._partition(arr, low, high)
        self._quick_sort(arr, low, pivotpos - 1)
        self._quick_sort(arr, pivotpos + 1, high)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) - 1
        self._quick_sort(nums, low, high)
        return nums[len(nums) - k]


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([3, 2, 1, 5, 6, 4], 2, 5),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
        ]
    )
