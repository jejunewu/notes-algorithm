from myDataStructure import TreeNode

def isSubStructure(A, B):
    def recur(A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return recur(A.left, B.left) and recur(A.right, B.right)

    return bool(A and B) and (recur(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B))


################### Test ########################
A = [1,2,3,4]
B = [3]
A = TreeNode.list2TreeNode(A)
B = TreeNode.list2TreeNode(B)
res = isSubStructure(A, B)
print(res)