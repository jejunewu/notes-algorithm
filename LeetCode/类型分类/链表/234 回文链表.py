from myDataStructure import ListNode

def isPalindrome(head) -> bool:

    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    for i in range(len(arr) >> 1):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

################### Test ########################
arr = [1,2,2,1]
head = ListNode.listToListNode(arr)
ans = isPalindrome(head)
print(ans)