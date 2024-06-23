from DataStructure import TreeNode

def mirrorTree(root):
    if not root:
        return

    tmp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(tmp)

    return root

################### Test ########################

root = [4,2,7,1,3,6,9]
root = TreeNode.list2TreeNode(root)
ans = mirrorTree(root)
ans = TreeNode.treeNode2List(ans)
print(ans)
