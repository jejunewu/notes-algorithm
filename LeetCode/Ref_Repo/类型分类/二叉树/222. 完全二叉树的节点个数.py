from myDataStructure import TreeNode

def countNodes(TreeNode):

    def dfs(root, level, res:[]):
        if root == None:
            return res
        if len(res) == level:
            res.append([root.val])
        else:
            res[level].append(root.val)

        res = dfs(root.left, level + 1, res)
        res = dfs(root.right, level + 1, res)
        return res

    ans = 0
    for i in dfs(TreeNode,0,[]):
        ans += len(i)
    return ans


################### Test ########################
root = [1,2,3,4,5,6]
root = TreeNode.list2TreeNode(root)
ans = countNodes(root)
print(ans)