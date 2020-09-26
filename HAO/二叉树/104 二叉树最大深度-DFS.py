import HAO.二叉树.str2TreeNode as st

TreeNode = st.TreeNode

def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    # print(maxDepth(root.left),'= = = = =', maxDepth(root.right))
    return max(maxDepth(root.left), maxDepth(root.right)) + 1



def maxDepth2(root: TreeNode) -> int:

    from collections import deque
    # import queue
    res = []
    stack = deque()
    stack.append(root)
    # print(stack)
    while(len(stack) != 0):
        # node = TreeNode()
        node = stack[-1]
        res.append(node.val)
        stack.pop()
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return res



s= '[3,4,20,null,null,15,7]'
print(s)

root = st.stringToTreeNode(s)
res = maxDepth2(root)

print(res)


def maxDepth3(root):
    if not root:
        return 0
    maxdepth = 0
    stack = [(root, 1)]
    while stack:
        curNode, layer = stack.pop()
        if not curNode.left and not curNode.right and layer > maxdepth:
                maxdepth = layer
        if curNode.right:
            stack.append((curNode.right, layer+1))
        if curNode.left:
            stack.append((curNode.left, layer+1))
    return maxdepth

print(maxDepth3(root))