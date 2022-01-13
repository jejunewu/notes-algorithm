from myDataStructure import TreeNode

def isSymmetric(root):
    tmp = [(root, root)]
    while tmp:
        L,R = tmp.pop(0)
        if not L and not R:
            continue
        if not L or not R:
            return False
        if L.val != R.val:
            return False
        tmp.append((L.left, R.right))
        tmp.append((L.right, R.left))
    return True

root = [1,2,2,3,4,4,3]
root = TreeNode.list2TreeNode(root)
ans = isSymmetric(root)
print(ans)