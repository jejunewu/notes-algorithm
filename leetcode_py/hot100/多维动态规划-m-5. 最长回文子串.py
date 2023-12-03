"""

5. 最长回文子串
提示
中等
7K
相关企业
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
通过次数
1.6M
提交次数
4.1M
通过率
37.9%

"""
"""超时

    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s):
            length = len(s)
            mid = length // 2
            pre = s[:mid]
            post = ''
            if length % 2 == 0:
                tmp = s[mid:]
            else:
                tmp = s[mid + 1:]
            for ch in tmp[::-1]:
                post += ch
            return pre == post

        length = len(s)
        max_len = 1
        res = s[0]
        for i in range(length-1):
            for j in range(i+1, length):
                sub_s = s[i:j+1]
                if isPalindrome(sub_s) and len(sub_s) > max_len:
                    max_len = len(sub_s)
                    res = sub_s
        return res
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        max_len, start = 1, 0

        for j in range(1, length):
            for i in range(j):
                if j - i <= 2:
                    # 情况1 ： 首尾相等 & <=2
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        if max_len < j - i + 1:
                            max_len = j - i + 1
                            start = i
                else:
                    # 情况2 ：>2 & 根据[i+1, j-1]子串判断是否回文
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        if max_len < j - i + 1:
                            max_len = j - i + 1
                            start = i
        return s[start:start + max_len]


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ("babad", "bab"),
            ("cbbd", "bb")
        ]
    )
