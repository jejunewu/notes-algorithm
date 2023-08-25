from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = [root]
    for value in preorder[1:]:
        if value is None:
            continue
        node = TreeNode(value)
        if value < stack[-1].val:
            stack[-1].left = node
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = node
        stack.append(node)
    return root


from collections import deque


def print_tree(root: TreeNode):
    if not root:
        print('Empty tree')
        return
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                level.append(' ')
        print(' '.join(level))


def list2TreeNode(inputValues):
    # input = input.strip()
    # input = input[1:-1]
    # if not input:
    #     return None
    #
    # inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNode2List(root):
    if not root:
        return "[]"
    output = []
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output.append(None)
            continue

        output.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    return output


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [1, 2, None, 2, 3]
    # node = build_tree(arr)

    # node = TreeNode(1)
    # print_tree(node)
    # print(node)
