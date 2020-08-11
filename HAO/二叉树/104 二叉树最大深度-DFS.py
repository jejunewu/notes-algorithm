import HAO.二叉树.str2TreeNode as st

TreeNode = st.TreeNode

def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    print(maxDepth(root.left),'= = = = =', maxDepth(root.right))
    return max(maxDepth(root.left), maxDepth(root.right)) + 1



def maxDepth2(root: TreeNode) -> int:

    from collections import deque
    # import queue
    res = []
    stack = deque()
    stack.append(root)
    print(stack)
    while(len(stack) != 0):
        # node = TreeNode()
        node = stack[0]
        res.append(node)
        stack.pop()
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return res



s= '[3,4,20,null,null,15,7]'
root = st.stringToTreeNode(s)

res = maxDepth2(root)
print(res)