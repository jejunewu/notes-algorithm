"""

206. 反转链表
简单
3.4K
相关企业
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import *
from utils.data_structure.ListNode import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:
            tmp = ListNode(head.val)
            tmp.next = res
            res = tmp
            head = head.next
        return res
