"""
206. 反转链表
简单
3.3K
相关企业
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
1 -> 2 -> 3 -> 4 -> 5
5 -> 4 -> 3 -> 2 -> 1

输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000


进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""

from DataStructure.ListNode import ListNode, list2ListNode, listNode2List
from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        创建tmp空间实现反转
        :param head:
        :return:
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    sol = Solution()

    cases = [
        (list2ListNode([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1]),
        (list2ListNode([1, 2]), [2, 1]),
        (list2ListNode([]), []),
    ]
    for idx, case in enumerate(cases):
        res = listNode2List(sol.reverseList(case[0]))
        print(f"case_id: {idx} || {case[1] == res} || {case[1]} || {res} ")
