from HAO.链表 import LinkedList as node


def addTwoNumbers(l1, l2):
    ans = node.ListNode(0)

    tmp = ans
    carry = 0
    idx = 0

    while l1 and l2:
        tmp.next = node.ListNode((carry + l1.val + l2.val)%10)
        tmp = tmp.next

        if l1.val + l2.val + carry> 9:
            carry = 1
        else:
            carry = 0

        l1 = l1.next
        l2 = l2.next
        idx += 1

    return ans.next
#######################
def addTwoNumbers2(l1, l2):
    ans = cur = node.ListNode(None)
    s = 0
    while l1 or l2 or s:
        s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        cur.next = node.ListNode(s % 10)
        cur = cur.next
        s//=10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return ans.next

l1 = [2,4,3]
l2 = [5,6,4]

l1 = node.listToListNode(l1)
l2 = node.listToListNode(l2)

# print(l1.next)


ans = addTwoNumbers2(l1, l2)
ans = node.ListNodeTolist(ans)
# t = 12%10
print(ans)
