from myDataStructure import ListNode

def deleteNode(head, val):
    tmp = ListNode.ListNode(None)
    tmp.next = head
    pos = head = tmp
    # pos = head

    while pos.next:
        if pos.next.val == val:

            if pos.next.next:
                pos.next = pos.next.next
            else:
                pos.next = None
                return head.next

        pos = pos.next

    return head.next

################### Test ########################
head = [-3,-9,-99]
val = -3

head = ListNode.list2ListNode(head)
ans = deleteNode(head, val)
ans = ListNode.listNode2List(ans)
print(ans)