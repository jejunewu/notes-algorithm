from HAO.二叉树 import str2TreeNode as tree

def kthLargest(root, k: int) -> int:

    def dfs(root, level,res):
        if root == None:
            return res

        if len(res) == level:
            res.append([root.val])
        else:
            res[level].append(root.val)

        res = dfs(root.left, level+1, res)
        res = dfs(root.right, level+1, res)
        return res

    ans = []
    for i in dfs(root, 0, []):
        for j in i:
           ans.append(j)
    return sorted(ans)[-1*k]


root = '[5,3,6,2,4,null,null,1]'
k = 3

root = tree.stringToTreeNode(root)
t = kthLargest(root, k)
print(t)

