"""
94. 二叉树的中序遍历
简单
2K
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

"""

from typing import Optional, List
from utils.data_structure import TreeNode

from utils.solution import solve_batch

"""
递归方法
"""
class Solution:

    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res


solve_batch(
    Solution,
    [

    ]
)
