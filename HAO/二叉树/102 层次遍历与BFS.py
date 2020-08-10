import HAO.二叉树.str2TreeNode as st

s = '[1,null,2,null,3,null,4,null,null]'
root = st.stringToTreeNode(s)
res = st.treeNodeToString(root)
print(res)
