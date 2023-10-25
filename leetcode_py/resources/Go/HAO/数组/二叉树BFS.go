package main
import "fmt"

func main() {
	levelOrder()
}
func levelOrder(root *TreeNode) [][]int {
return dfs(root, 0, [][]int{})
}
func dfs(root *TreeNode, level int, res [][]int) [][]int {
if root == nil {
return res
}
if len(res) == level {
res = append(res, []int{root.Val})
} else {
res[level] = append(res[level], root.Val)
}
res = dfs(root.Left, level+1, res)
res = dfs(root.Right, level+1, res)
return res
}