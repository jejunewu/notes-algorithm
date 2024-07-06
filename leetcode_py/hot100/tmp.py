from typing import List


class Solution:
    """ 用二分查找方法 """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return r



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
