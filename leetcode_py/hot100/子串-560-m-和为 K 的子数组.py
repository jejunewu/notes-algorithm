"""

560. 和为 K 的子数组
提示
中等
2.1K
相关企业
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from typing import List


class Solution:
    """
    暴力枚举-超内存

     def list_sub_arr(self, nums):
         sub_arr = []
         for i in range(len(nums)):
             for j in range(i, len(nums)):
                 sub_arr.append(nums[i:j + 1])
         return sub_arr

     def subarraySum(self, nums: List[int], k: int) -> int:
         ans = 0
         for item in self.list_sub_arr(nums):
             if item and sum(item) == k:
                 ans += 1
         return ans
     """

    """
    前缀和+hash
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        count_dict = {0: 1}
        sums, res = 0, 0
        for n in nums:
            sums += n
            if sums - k in count_dict:
                res += count_dict[sums - k]
            if sums in count_dict:
                count_dict[sums] += 1
            else:
                count_dict[sums] = 1
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ([0, 0], 0, 3),
        ([1, -1, 0], 0, 3),
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),

    ]

    solve_batch(
        Solution,
        cases,
    )
