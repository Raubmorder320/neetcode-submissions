func searchInsert(nums []int, target int) int {

	i, j := 0, len(nums)-1
	m := 0
	for i <= j {
		m = i + (j-i)/2
		if nums[m] < target {
			i = m + 1
		} else if nums[m] > target {
			j = m - 1
		} else {
			i = m
			break
		}
	}

	return i

}
