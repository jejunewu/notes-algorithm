"""
3. 无重复字符的最长子串
中等
9.5K
相关企业
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



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


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑窗法
        :param s:
        :return:
        """
        if len(s) < 2:
            return len(s)
        start_idx = 0
        max_len = 1
        while len(s) - start_idx > max_len and start_idx < len(s) - 1:
            for end_idx in range(start_idx + max_len, len(s) + 1):
                if len(set(s[start_idx:end_idx])) != len(s[start_idx:end_idx]):
                    break
                if len(set(s[start_idx:end_idx])) > max_len:
                    max_len = len(set(s[start_idx:end_idx]))
            start_idx += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()

    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("p", 1),
        ("aa", 1),
        ("aaa", 1),
        ("", 0),
        ("au", 2)
    ]
    for idx, case in enumerate(cases):
        res = sol.lengthOfLongestSubstring(case[0])
        print(f"case_id: {idx} || {case[1] == res} || {case[1]} || {res} ")
