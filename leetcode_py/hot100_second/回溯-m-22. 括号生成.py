"""
22. 括号生成
已解答
中等
相关标签
相关企业
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8

"""
from utils import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s: str, left: int, right: int):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        res = []
        backtrack('', 0, 0)
        return res
        # return []


if __name__ == '__main__':
    solve_batch(
        Solution, [
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        ]
    )
