from HAO.二叉树 import str2TreeNode as tree

# tree.TreeNode()



def isValidBST(root):

    import math
    if root == None:
        return True

    return isBST(root, float('-inf'), float('inf'))

def isBST(root, Min, Max):
    if root == None:
        return True
    if root.val <= Min or root.val >= Max:
        return False

    return isBST(root.left, Min, root.val) and isBST(root.right, root.val, Max)

root = '[2,1,3]'
root = tree.stringToTreeNode(root)
t = isValidBST(root)
print(t)
