"""

20. 有效的括号
提示
简单
4.2K
相关企业
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if stack and ((stack[-1] == '(' and item == ')') or (stack[-1] == '[' and item == ']') or (
                    stack[-1] == '{' and item == '}')):
                stack.pop(-1)
            else:
                stack.append(item)
        return len(stack) == 0


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ("()", True),
            ("(]", False),
            ("()[]{}", True)
        ]
    )
