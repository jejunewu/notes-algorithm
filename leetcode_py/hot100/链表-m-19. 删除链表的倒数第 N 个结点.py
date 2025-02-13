# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

19. 删除链表的倒数第 N 个结点
已解答
中等
相关标签
相关企业
提示
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。



示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


进阶：你能尝试使用一趟扫描实现吗？

"""

from utils import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # node_reverse = ListNode(None)
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        node_list.pop(len(node_list) - 2)
        pivot = ListNode(None, head)
        for i in node_list:
            pivot.next = ListNode(i)
            pivot = pivot.next
        return pivot


cases = [
    (list2ListNode([1, 2, 3, 4, 5]), 2, list2ListNode([1, 2, 3, 5])),
]

solve_batch(Solution, cases)
