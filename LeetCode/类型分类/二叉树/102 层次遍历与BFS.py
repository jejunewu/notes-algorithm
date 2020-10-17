from myDataStructure import TreeNode as node


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

################################################
import collections
def levelOrder2(root):
    if not root:
        return root

    res = []
    # 初始化队列同时将第一层节点加入队列中，即根节点
    Q = collections.deque([root])
    # 外层的 while 循环迭代的是层数
    while Q:
        print(Q)
        # 记录当前队列大小
        size = len(Q)
        print(size)
        # 遍历这一层的所有节点
        for i in range(size):
            # 从队首取出元素
            node = Q.popleft()
            # 连接
            if i < size - 1:
                pass
                res.append(node.val)
                # node.next = Q[0]
            # 拓展下一层节点
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    # 返回根节点
    return res



# s = '[3,9,20,null,null,15,7]'
s = [1,2,3,4]
root = node.listToTreeNode(s)
# res = st.treeNodeToString(root)

# res = levelOrder(root)

res = levelOrder2(root)

print(res)