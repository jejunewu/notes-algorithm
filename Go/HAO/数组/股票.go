package main
import "fmt"


func max(a,b int) int {
if a > b {
return a
}
return b
}


func main()  {
	var prices = []int{7, 1, 5, 3, 6, 4}
	dp := make([][2]int, len(prices))

	fmt.Println(dp)
}
