from myDataStructure import TreeNode

def buildTree(preorder:list, inorder: list) -> TreeNode:
    if len(preorder) == 0:
        return None
    idx = inorder.index(preorder[0])
    print(idx)
    root = TreeNode.TreeNode(preorder[0])
    left = buildTree(preorder[1:idx+1], inorder[:idx])
    right = buildTree(preorder[idx+1:], inorder[idx+1:])
    root.left = left
    root.right = right
    return root


################### Test ########################
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


ans = buildTree(preorder,inorder)
print(ans)