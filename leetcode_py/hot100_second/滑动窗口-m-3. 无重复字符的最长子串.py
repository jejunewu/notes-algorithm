"""
3. 无重复字符的最长子串
已解答
中等
相关标签
相关企业
提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

'''
两次循环，判断一些特殊情况，比如""、 "a"
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        res = 1
        for i in range(n):
            for j in range(i + 1, n):
                sub_s = s[i:j]
                if s[j] in sub_s:
                    break
                else:
                    res = max(res, j - i + 1)
        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    cases = [
        ("au", 2),
        (" ", 1),
        ("", 0),
        ("abcabcbb", 3,),
        ("pwwkew", 3,),
        ("bbbb", 1),
    ]
    solve_batch(Solution, cases)
