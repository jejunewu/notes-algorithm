import HAO.二叉树.str2TreeNode as st
root = st.TreeNode



def dfs(root, level, res:[]):
    if root == None:
        return res

    if len(res) == level:
        res.append([root.val])
    else:
        res[level].append(root.val)

    res = dfs(root.left, level+1, res)
    res = dfs(root.right, level+1, res)
    return res

def levelOrder(root) :

    return dfs(root, 0, res=[])


# s = '[3,9,20,null,null,15,7]'
s = '[]'
root = st.stringToTreeNode(s)
# res = st.treeNodeToString(root)

res = levelOrder(root)

print(res)