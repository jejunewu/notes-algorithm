from DataStructure import ListNode

def mergeTwoLists(l1, l2):
    res = ListNode.ListNode(1)
    cur = res
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = ListNode.ListNode(l1.val)
            l1 = l1.next
        else:
            cur.next = ListNode.ListNode(l2.val)
            l2 = l2.next
        cur = cur.next
    if not l1:
        cur.next = l2
    if not l2:
        cur.next = l1

    return res.next

################### Test ########################
l1 = [-9,3]
l2 = [5,7]
l1 = ListNode.list2ListNode(l1)
l2 = ListNode.list2ListNode(l2)

res = mergeTwoLists(l1, l2)
res = ListNode.listNode2List(res)
print(res)