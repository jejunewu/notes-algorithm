"""

56. 合并区间
中等
2.2K
相关企业
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for sub_list in sorted(intervals, key=lambda x: x[0]):
            # 如果当前区间的起始位置大于res[-1]的结束位置，则将当前区间加入res中，否则更新res[-1]的结束位置为当前区间的结束位置
            if not res or res[-1][1] < sub_list[0]:
                res.append(sub_list)
            else:
                res[-1][1] = max(res[-1][1], sub_list[1])
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([[1, 4], [0, 4]], [[0, 4]]),
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]])
        ]
    )
