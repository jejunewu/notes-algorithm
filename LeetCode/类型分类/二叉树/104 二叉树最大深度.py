class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        print(self.maxDepth(root.left),'= = = = =', self.maxDepth(root.right))
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
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


def main():
    import sys
    import io
    # def readlines():
    #     for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
    #         yield line.strip('\n')
    #
    # lines = readlines()
    # while True:
    #     try:
    # line = next(lines)
    line = '[3,9,20,null,null,15,7]'
    root = stringToTreeNode(line);

    ret = Solution().maxDepth(root)

    out = str(ret);
    print(out)
        # except StopIteration:
        #     break


if __name__ == '__main__':
    main()