from HAO.二叉树 import str2TreeNode as tree


def Traversal(root):
    def preorder(root):
        if root == None:
            return
        preres.append(root.val)
        preorder(root.left)
        preorder(root.right)

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        inres.append(root.val)
        inorder(root.right)

    def postorder(root):
        if root == None:
            return
        postorder(root.left)
        postorder(root.right)
        postres.append(root.val)

    preres, inres, postres = [], [], []
    # preorder(root)
    inorder(root)
    # postorder(root)

    return [preres, inres, postres]



s = '[1,null,2,3]'

root = tree.stringToTreeNode(s)

t = Traversal(root)
print(t)
