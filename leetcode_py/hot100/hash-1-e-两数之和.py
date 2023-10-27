from typing import List


# 用hash方法做

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, n in enumerate(nums):
            if target - n in hashtable:
                return [i, hashtable[target - n]]
            hashtable[n] = i


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
    solve_batch(
        Solution, cases
    )
