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

'''
解法一：暴力循环
超时

解法二：前缀和hash
把前缀和保存到字典，类似两数之和的解法，只需一次遍历
'''

"""
def subarraySum(self, nums: List[int], k: int) -> int:
    count_dict={0:1} # 键是n-k，值是次数，设个0::1，目的是为了碰到单个元素为0
    s, res = 0, 0
    for n in nums:
        s+=n
        if s-k  in count_dict:
            res += count_dict[s-k]
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1 
    return res  
"""

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        res = 0
        sums = 0
        for n in nums:
            sums += n
            if sums - k in prefix_sum:
                res += prefix_sum[sums - k]
            if sums in prefix_sum:
                prefix_sum[sums] += 1
            else:
                prefix_sum[sums] = 1

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
