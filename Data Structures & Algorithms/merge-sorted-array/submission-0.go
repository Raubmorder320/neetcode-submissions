func merge(nums1 []int, m int, nums2 []int, n int) {
	copy(nums1[m:], nums2)
	copy(nums1, mergeSort(nums1))
}

func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := len(arr) / 2
	arr1 := mergeSort(arr[:mid])
	arr2 := mergeSort(arr[mid:])
	arr = m(arr1, arr2)
	return arr
}
func m(arr1 []int, arr2 []int) []int {
	i, j := 0, 0
	res := make([]int, 0, len(arr1)+len(arr2))
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			res = append(res, arr1[i])
			i++
		} else {
			res = append(res, arr2[j])
			j++
		}
	}
	res = append(res, arr1[i:]...)
	res = append(res, arr2[j:]...)
	return res
}
