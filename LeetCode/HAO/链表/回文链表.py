from HAO.链表 import LinkedList as ll

l = [1,2,2,1]
head = ll.listToListNode(l)

stack = []
while head:
    stack.append(head.val)
    head = head.next


print(stack)