"""

739. 每日温度
提示
中等
1.7K
相关企业
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。



示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]


提示：

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""

from typing import *


class Solution:
    '''超时
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures) - 1):
            cur_t = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > cur_t:
                    res.append(j - i)
                    break
                elif j == len(temperatures) - 1:
                    res.append(0)
        return res + [0]
    '''

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return []


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0])
        ]
    )
