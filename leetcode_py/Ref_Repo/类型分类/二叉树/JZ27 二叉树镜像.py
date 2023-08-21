from HAO.二叉树 import str2TreeNode as tree

def mirrorTree(root):
    def dfs(root, level, res):
        if root == None:
            return res
        if len(res) == level:
            res.append([root.val])
        else:
            res[level].insert(0, root.val)
        res = dfs(root.left, level + 1, res)
        res = dfs(root.right, level + 1, res)
        return res

    tmp = dfs(root, 0, [])
    ans = []
    for i in tmp:
        for j in i:
            ans.append(j)
    return ans

root = tree.stringToTreeNode('[4,2,7,1,3,6,9]')
ans = mirrorTree(root)
# t = tree.treeNodeToString(ans)
print(ans)

def mirrorTree2(root):
    if not root:
        return
    tmp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(tmp)
    return root

root = tree.stringToTreeNode('[4,2,7,1,3,6,9]')
ans = mirrorTree2(root)
# t = tree.treeNodeToString(ans)
print(ans)

