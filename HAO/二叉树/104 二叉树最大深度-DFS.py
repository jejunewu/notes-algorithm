import HAO.二叉树.str2TreeNode as st

TreeNode = st.TreeNode

def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    print(maxDepth(root.left),'= = = = =', maxDepth(root.right))
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


s= '[3,4,20,null,null,15,7]'
root = st.stringToTreeNode(s)

res = maxDepth(root)
print(res)