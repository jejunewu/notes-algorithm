package main

import "fmt"

func main()  {

	fmt.Println("Go - Start")
	var nums1 =[3]int{4,9,5}
	var nums2 =[5]int{9,4,9,8,4}

	var res []int
	res = intersect(nums1 , nums2)
	fmt.Println(res)
}


//GO
func intersect(nums1 [3]int, nums2 [5]int) []int {
	m0 := map[int]int{}
	for _, v := range nums1 {
		//遍历nums1，初始化map
		m0[v] += 1
		fmt.Println(v)
}
	k := 0
	for _, v := range nums2 {
		//如果元素相同，将其存入nums2中，并将出现次数减1
		if m0[v] > 0 {
			m0[v] -= 1
			nums2[k] = v
			k++
		}
	}
	return nums2[0:k]
}
