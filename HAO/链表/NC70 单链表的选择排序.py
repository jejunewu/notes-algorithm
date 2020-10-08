from HAO.链表 import LinkedList as node

def sortInList(head):
    arr = []
    p = head
    while p:
        arr.append(p.val)
        p = p.next

    arr.sort()
    p = head
    for i in arr:
        p.val = i
        p = p.next

    return head

head = [1,3,2,4,5]
head = node.listToListNode(head)

ans = sortInList(head)
ans = node.ListNodeTolist(ans)
print(ans)