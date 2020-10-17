from myDataStructure import ListNode

def swapPairs(head):

    pos = ListNode.ListNode(None)
    pos.next = head
    c = pos
    while c.next and c.next.next:
        a,b = c.next, c.next.next
        c.next = b
        a.next = b.next
        b.next = a
        c = c.next.next
    return pos.next


#    while head and head.next:
    #        cur.next = cur.next.next
    #        head = head.next
    return cur

head= [1, 2, 3, 4]
head = ListNode.listToListNode(head)
ans = swapPairs(head)
ans = ListNode.listNodeToList(ans)
print(ans)