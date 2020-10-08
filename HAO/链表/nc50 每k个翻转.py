from HAO.链表 import LinkedList as node

def reverseKGroup(head , k):
    # write code here
    count = 0
    # cur = node.ListNode(None)
    while count < k:
        # cur.next = head
        head = head.next
        count+=1

    head.next = None
    cur = head

    return cur



l = [1,2,3,4]
head = node.listToListNode(l)
k = 2

cur = head

head = head.next
cur.next = head

head = head.next
cur.next = head

cur.next = None
# tmp = head.next.next
# head.next.next = None
# cur = tmp

tList = node.ListNodeTolist(cur)

print(tList)

# cur = node.ListNode(None)
# cur.next = head
# cur.next = head.next
# cur.next = None

# print(node.ListNodeTolist(head))
# print(node.ListNodeTolist(cur))

