from HAO.二叉树 import str2TreeNode as tree

def pathSum(root, sum):
    pass


#######################
List, sum = '[5,4,8,11,null,13,4,7,2,null,null,5,1]', 22
root = tree.stringToTreeNode(List)
print(root.val)

def pathSum(root, sum):

    res = list()
    path = list()

    def dfs(root, sum):
        if not root:
            return
        path.append(root.val)
        sum-=root.val
        if not root.left and not root.right and sum == 0:
            res.append(path[:])
        dfs(root.left, sum)
        dfs(root.right, sum)
        path.pop()


    dfs(root, sum)
    return res

t = pathSum(root,sum)
print(t)