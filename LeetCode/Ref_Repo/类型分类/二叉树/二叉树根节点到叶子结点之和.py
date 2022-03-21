from DataStructure import TreeNode as tree

def sumNumbers(root):
    # write code here
    if not root:
        return 0

    def dfs(path, root, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
        if root.left:
            res = dfs(path + str(root.val), root.left, res)
        if root.right:
            res = dfs(path + str(root.val), root.right, res)
        return res

    # return sum([int(i) for i in dfs('', root,[])])
    ans = dfs('', root,[])
    return ans

root = [1,2,3]
root = tree.list2TreeNode(root)
t = sumNumbers(root)
print(t)