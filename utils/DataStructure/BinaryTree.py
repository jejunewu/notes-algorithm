from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list2Tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """ 数组 --> 二叉树 """
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


def tree2List(root: TreeNode) -> List[List[int]]:
    if not root: return []
    res, queue = [], deque()
    queue.append(root)
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp)
    return res


def print_tree(root: TreeNode):
    print(tree2List(root))


if __name__ == '__main__':
    root = list2Tree([1, 2, None, 3, 4])
    # res = print(root)
    # print(res)
    print_tree(root)
