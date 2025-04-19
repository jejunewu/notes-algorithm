"""
287. 寻找重复数
已解答
中等
相关标签
相关企业
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3




提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次


"""

'''

'''
from utils import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val = 1
        max_val = len(nums)
        while min_val < max_val:
            mid_val = (min_val + max_val) // 2
            cnt = sum(min_val <= n <= mid_val for n in nums)

            if cnt > mid_val - min_val + 1:
                max_val = mid_val
            else:
                min_val = mid_val + 1
        return min_val


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution, [
            ([1, 3, 4, 2, 2], 2),
            ([3, 1, 3, 4, 2], 3)
        ]
    )
