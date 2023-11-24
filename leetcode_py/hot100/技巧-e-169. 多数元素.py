"""

169. 多数元素
简单
2K
相关企业
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2


提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_val = nums[0]
        max_counter = counter = 1
        for l, r in zip(nums[:-1], nums[1:]):
            if l == r:
                counter += 1
                continue
            elif counter > max_counter:
                max_counter = counter
                max_val = l
            counter = 1
        if counter > max_counter:
            max_val = l
        return max_val


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([2], 2),
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2)
        ]
    )
