from DataStructure import ListNode

def sortList(head):

    pos = head
    arr = []
    while pos:
        arr.append(pos.val)
        pos = pos.next
    arr.sort()
    print(arr)

    a = ListNode.ListNode(0)
    b = a
    for e in arr:
        b.next = ListNode.ListNode(e)
        b = b.next
    b = a.next
    return b

################### Test ########################

head = [8,6,5,7,6,7,5]
head = ListNode.list2ListNode(head)

ans = sortList(head)
ans = ListNode.listNode2List(ans)
print(ans)

