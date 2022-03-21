from DataStructure.ListNode import ListNode, list2ListNode, listNode2List


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    pre = ListNode(None)
    cur = pre
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = ListNode(list1.val)
            list1 = list1.next
        else:
            cur.next = ListNode(list2.val)
            list2 = list2.next
        cur = cur.next

    # 合并剩余
    cur.next = list1 if list1 else list2
    return pre.next

def mergeTwoLists2(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

l1 = [1, 2, 4]
l2 = [1, 3, 4]

l1 = list2ListNode(l1)
l2 = list2ListNode(l2)
node = mergeTwoLists2(l1, l2)
ans = listNode2List(node)
print(ans)
