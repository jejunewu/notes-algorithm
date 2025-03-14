"""
17. 电话号码的字母组合
已解答
中等
相关标签
相关企业
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

"""
from typing import List

'''
阶梯
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number2letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in number2letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        res = []
        backtrack("", digits)
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    ]
    solve_batch(Solution, cases)
