from DataStructure.ListNode import ListNode, list2ListNode, listNode2List


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    ans = ListNode(None)
    cur =None
    while list1 and list2:
        if list1.val < list2.val:
            ans.next = ListNode(list1.val)
            list1 = list1.next
            cur = ans

        else:
            ans.next = ListNode(list2.val)
            list2 = list2.next
    return ans


l1 = [1, 2, 4]
l2 = [1, 3, 4]

l1 = list2ListNode(l1)
l2 = list2ListNode(l2)
node = mergeTwoLists(l1, l2)
ans = listNode2List(node)
print(ans)