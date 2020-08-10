# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listToListNode(List):
    tem_node = ListNode(None)
    node = ListNode(None)
    for i in List:
        # 记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = ListNode(i)
            tem_node = tem_node.next
    return node


def ListNodeTolist(head: ListNode) -> list:
    List = []
    while head:
        List.append(head.val)
        head = head.next
    return List


a = [1, 2, 3]
res = listToListNode(a)
List = ListNodeTolist(res)

print(List)