"""
94. 二叉树的中序遍历
简单
1.9K
相关企业
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。



示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

from typing import Optional, List
from DataStructure.BinaryTree import *


class Solution:
    # 递归求解
    def inorder(self, root: Optional[TreeNode], res: list):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    cases = [
        (TreeNode([1, None, 2, 3]), [1, 3, 2]),
        (TreeNode([]), []),
        (TreeNode([1]), [1]),
    ]
    for idx, case in enumerate(cases):
        res = list2Tree(sol.inorderTraversal(case[0]))
        res = tree2List(res)
        print(f"case_id: {idx} || {case[1] == res} || {case[1]} || {res} ")
