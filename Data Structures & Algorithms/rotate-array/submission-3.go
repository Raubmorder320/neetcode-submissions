func rotate(nums []int, k int) {
	j:=len(nums)-1
	k=k%len(nums)
	for i:=0; i<j; i++{
		nums[i], nums[j] = nums[j], nums[i]
		j--
	}
	j=k-1
	for i:=0; i<j; i++{
		nums[i], nums[j] = nums[j], nums[i]
		j--
	}
	j=len(nums)-1
	for i:=k; i<j; i++{
		nums[i], nums[j] = nums[j], nums[i]
		j--
	}
}
