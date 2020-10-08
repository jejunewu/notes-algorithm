from HAO.链表 import LinkedList as node

def FindFirstCommonNode(pHead1 , pHead2 ):

    p1,p2 = pHead1,pHead2

    while p1 != p2:
        p1 = p1.next if p1 else pHead2
        p2 = p2.next if p2 else pHead1

    return p1


pHead1 , pHead2 = [0, 1,3,5], [9,1,2,7]

pHead1 , pHead2 = node.listToListNode(pHead1), node.listToListNode(pHead2)

ans = FindFirstCommonNode(pHead1 , pHead2)
print(ans)