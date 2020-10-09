from myDataStructure import ListNode


def reversePrint(head: ListNode):
    res = []
    while head:
        res.insert(0,head.val)
        head = head.next
    return res


################### Test ########################
head = [1,3,2]
head = ListNode.listToListNode(head)

ans = reversePrint(head)
print(ans)
