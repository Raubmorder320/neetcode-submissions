func removeDuplicates(nums []int) int {
	i,j:=0,1
	k:=1
	for i<len(nums) && j<len(nums){
		if nums[j]!=nums[i]{
			i++
			nums[i]=nums[j]
			k++
		}
		j++
	}
	return k
}
