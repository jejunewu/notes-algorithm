class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2ListNode(numbers: list):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNode2List(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def check_nodes_is_same(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

if __name__ == '__main__':
    l1 = list2ListNode([1, 2, 3])
    l2 = list2ListNode([1, 2, 3])
    res =  check_nodes_is_same(l1, l2)
    print(res)
