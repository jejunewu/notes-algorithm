from HAO.二叉树 import str2TreeNode as tree


def averageOfLevels(root):
    ans = []
    for i in dfs(root, 0, []):
        ans.append(sum(i)/len(i))
    return ans


def dfs(root, level, res):
    if root == None:
        return res

    if len(res) == level:
        res.append([root.val])
    else:
        res[level].append(root.val)

    res = dfs(root.left, level+1, res)
    res = dfs(root.right, level+1, res)
    return res

root = tree.stringToTreeNode('[3,9,20,15,7]')

s = averageOfLevels(root)

print(s)