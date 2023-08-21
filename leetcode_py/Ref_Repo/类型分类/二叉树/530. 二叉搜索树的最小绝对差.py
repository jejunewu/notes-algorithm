from DataStructure import TreeNode

def getMinimumDifference(root) -> int:

    def dfs(MIN, root):
        if not root:
            return 0
        if root.left:
            MIN = min(MIN, abs(root.val-root.left.val))
        if root.right:
            MIN = min(MIN, abs(root.val-root.right.val))

        root.left = dfs(MIN,root.left)
        root.right = dfs(MIN,root.right)
        return MIN

    MIN = 0
    if root.left:
        MIN = abs(root.val-root.left.val)
    elif root.right:
        MIN = abs(root.val-root.right.val)

    return dfs(MIN,root)



def getMinimumDifference2(root) -> int:

    ans = float('inf')
    pre = -1

    def dfs(root):
        nonlocal ans, pre
        if not root:
            return
        dfs(root.left)
        if pre != -1:
            ans = min(ans, root.val - pre)
        pre = root.val
        dfs(root.right)

    dfs(root)
    return ans


arr = [1,4,3,2]
root = TreeNode.listToTreeNode(arr)
# print(root.left.val)
ans = getMinimumDifference2(root)
print(ans)