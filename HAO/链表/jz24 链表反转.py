from HAO.链表 import LinkedList as ll

def reverseList(head):
    # cur = ll.ListNode(None)
    cur = None
    while head:
        tmp = ll.ListNode(head.val)
        tmp.next = cur
        cur = tmp
        head = head.next

    return cur


def reverse(head):
    cur = None
    while head:
        tmp = head.next
        head.next = cur
        cur = head
        head = tmp
    return cur




l = [1,2,3,4,5]
head = ll.listToListNode(l)
head_ans = reverse(head)
l2 = ll.ListNodeTolist(head_ans)


# print(l2)