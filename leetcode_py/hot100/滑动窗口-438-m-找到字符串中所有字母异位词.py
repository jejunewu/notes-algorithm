"""
438. 找到字符串中所有字母异位词
中等
1.3K
相关企业
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母

"""

from typing import *


class Solution:

    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     """ 超时 """
    #     p_len = len(p)
    #     p_sort = sorted(p).__str__()
    #     res = []
    #     for i in range(0, len(s) - p_len + 1):
    #         sub = s[i:i + p_len]
    #         if sorted(sub).__str__() == p_sort:
    #             res.append(i)
    #     return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)  # 获取p的长度
        s_len = len(s)  # 获取s的长度
        count_p = [0] * 26  # 初始化p的计数器
        count_s = [0] * 26  # 初始化滑动窗口s的计数器
        res = []  # 初始化结果列表

        if p_len > s_len:
            return res

        # 计算p中每个字符的出现次数
        for i in range(p_len):
            count_p[ord(p[i]) - ord('a')] += 1
            count_s[ord(s[i]) - ord('a')] += 1

        # 如果p的计数器和滑动窗口的计数器相等，将0添加到结果列表中
        if count_p == count_s:
            res.append(0)

        # 遍历s中剩余的字符
        for i in range(p_len, s_len):
            count_s[ord(s[i]) - ord('a')] += 1  # 增加新字符的计数
            count_s[ord(s[i - p_len]) - ord('a')] -= 1  # 减去最左边字符的计数

            if count_p == count_s:
                res.append(i - p_len + 1)

        return res


if __name__ == '__main__':
    from utils.solution import solve_batch

    solve_batch(
        Solution,
        [
            ("aaaaaaaaaa", "aaaaaaaaaaaaa", [])
            # ("cbaebabacd", "eba", [0, 6]),
            # ("abab", "ab", [0, 1, 2])
        ]
    )
