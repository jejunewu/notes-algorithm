from myDataStructure import ListNode

def oddEvenList(head):
    if not head:
        return head

    evenHead = head.next
    odd, even = head, evenHead
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    return head

################### Test ########################
head = [1,2,3,4,5]
head = ListNode.list2ListNode(head)
ans = oddEvenList(head)
ans = ListNode.listNode2List(ans)
print(ans)