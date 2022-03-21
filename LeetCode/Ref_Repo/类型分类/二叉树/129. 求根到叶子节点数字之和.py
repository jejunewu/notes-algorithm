from DataStructure import TreeNode

def sumNumbers(root) :
    if not root:
        return 0

    def dfs(root, path, res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            res = dfs(root.left, path+str(root.val), res)
        if root.right:
            res = dfs(root.right, path + str(root.val), res)
        return res

    return sum(map(int, dfs(root, '', [])))



################### Test ########################
root = [1,2,3]
root = TreeNode.list2TreeNode(root)
ans = sumNumbers(root)
print(ans)