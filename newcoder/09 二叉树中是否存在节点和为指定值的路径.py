from myDataStructure import TreeNode

def hasPathSum(root , Sum):
    # write code here

    def dfs(path:list, root, res):
        if not root.left and not root.right:
            res.append(path+[root.val])
        if root.left:
            res = dfs(path+[root.val], root.left, res)
        if root.right:
            res = dfs(path+[root.val], root.right, res)
        return res

    for i in dfs([], root, []):
        if sum(i) == Sum:
            return True
    return False


root = TreeNode.listToTreeNode([])
ans = hasPathSum(root, 1)
print(ans)