
from HAO.二叉树 import str2TreeNode as st

def isBalanced(root) -> bool:
    if root == None:
        return True
    if not isBalanced(root.left) or not isBalanced(root.right):
        return False
    leftH = maxDepth(root.left)+1
    rightH = maxDepth(root.right)+1

    if abs(leftH -rightH) > 1:
        return False
    return True


def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left), max(root.right)) +1