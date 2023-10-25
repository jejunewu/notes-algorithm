from HAO.二叉树 import str2TreeNode as tree

def insertIntoBST(root, val):
    if root == None:
        return tree.TreeNode(val)
    pos = root
    while pos:
        if val < pos.val:
            if not pos.left:
                pos.left = tree.TreeNode(val)
                break
            else:
                pos = pos.left
        else:
            if not pos.right:
                pos.right = tree.TreeNode(val)
                break
            else:
                pos = pos.right

    return root



s = '[4, 2, 7, 1, 3]'
val = 5
root = tree.stringToTreeNode(s)

root = insertIntoBST(root, val)
ss = tree.treeNodeToString(root)
print(ss)