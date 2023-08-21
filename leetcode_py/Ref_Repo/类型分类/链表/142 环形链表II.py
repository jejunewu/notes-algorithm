from DataStructure import ListNode

def detectCycle(head: ListNode) -> ListNode:
    fast, slow = head, head
    while True:
        if not (fast and fast.next):
            return
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast


head = [3,2,0,-4]
head = ListNode.listToListNode(head)
ans = detectCycle(head)

print(ans)