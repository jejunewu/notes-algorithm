class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2ListNode(numbers:list):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNode2List(head):
    res= []
    while head:
        res.append(head.val)
        head = head.next
    return res