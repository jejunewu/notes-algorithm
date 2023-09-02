"""
1. 两数之和
提示
简单
17.6K
相关企业
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
 

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""

from typing import List

class Solution:
    #　暴力枚举O(N^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            pop_nums = nums.copy()
            pop_nums.pop(idx1)
            for idx2, num2 in enumerate(pop_nums):
                if num1 + num2 == target:
                    return [idx1, idx2+1]
    
if __name__ == '__main__':
    sol = Solution()

    cases = [
        (([2,7,11,15], 9), [0,1]),
        (([3,2,4], 6), [1,2]),
        (([3,3],6), [0,1])
    ]
    for idx, case in enumerate(cases):
        res = sol.twoSum(case[0][0], case[0][1])
        print(f"case_id: {idx} || {case[1] == res} || {case[1]} || {res} ")