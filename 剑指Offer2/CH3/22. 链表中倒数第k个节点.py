from DataStructure import ListNode

def getKthFromEnd(head, k):

    i = 0
    fast = slow = head
    while i<k:
        fast = fast.next
        i+=1

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


################### Test ########################
head = list(range(1,6))
head = ListNode.list2ListNode(head)
k = 2
ans = getKthFromEnd(head, k)
ans  = ListNode.listNode2List(ans)
print(ans)