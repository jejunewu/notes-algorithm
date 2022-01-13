from myDataStructure import ListNode

def reorderList(head):

    if not head:
        return None
    arr = []
    node = head
    while node:
        arr.append(node)
        node = node.next

    i, j = 0, len(arr) - 1
    while i < j:
        arr[i].next = arr[j]
        i += 1
        if i == j:
            break
        arr[j].next = arr[i]
        j -= 1

    arr[i].next = None


################### Test ########################
head = [1,2,3,4]
head = ListNode.listToListNode(head)
reorderList(head)

ans = ListNode.listNodeToList(head)
print(ans)