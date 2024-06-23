from DataStructure import TreeNode

def isSymmetric(root) -> bool:

    # 通过设置对称遍历一致性来判断
    def isSymm(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return isSymm(root1.left, root2.right) and isSymm(root1.right, root2.left)

    return isSymm(root, root)



################### Test ########################

root = [8,6,5,7,6,7,5]
root = TreeNode.list2TreeNode(root)
ans = isSymmetric(root)
print(ans)