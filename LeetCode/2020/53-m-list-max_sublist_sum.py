'''
 * 53. 最大子数组和
中等
6.3K
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


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        max_sum = sum(nums)
        while l < r:
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
            if sum(nums[l:r + 1]) > max_sum:
                max_sum = sum(nums[l:r + 1])
                print(nums[l:r + 1])

        return max_sum


if __name__ == '__main__':
    sol = Solution()

    cases = [
        # ([-2, 1], 1),
        # ([5, 4, -1, 7, 8], 23),
        ([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4], 6)
    ]
    for case in cases:
        res = sol.maxSubArray(case[0])
        print(f"{case[1]} || {res} || {case[1] == res}")
