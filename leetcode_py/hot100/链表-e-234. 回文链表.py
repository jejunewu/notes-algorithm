"""

234. 回文链表
简单
1.8K
相关企业
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

通过次数
660.3K
提交次数
1.2M
通过率
53.7%
请问您在哪类招聘中遇到此题？
1/5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import *
from utils.data_structure.ListNode import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        length = len(arr)
        for i in range(length // 2):
            if arr[i] != arr[length - i - 1]:
                return False
        return True
