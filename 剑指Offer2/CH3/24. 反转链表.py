from myDataStructure import ListNode

def reverseList(head):
    if not head:
        return None

    tmp = ListNode.ListNode(head.val)
    head = head.next
    while head:
        pos = ListNode.ListNode(head.val)
        pos.next = tmp
        tmp = pos
        head = head.next
    return pos

################### Test ########################
head = [1,2,3,4,5]
head = ListNode.list2ListNode(head)
ans = reverseList(head)
ans = ListNode.listNode2List(ans)
print(ans)