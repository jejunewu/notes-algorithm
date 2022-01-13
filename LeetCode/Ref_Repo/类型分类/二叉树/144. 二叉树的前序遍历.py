from myDataStructure import TreeNode

def preorderTraversal(root):

    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)

    res=[]
    preorder(root)
    return res

################### Test ########################

root = TreeNode.listToTreeNode([1,3,2,3])
ans = preorderTraversal(root)
print(ans)