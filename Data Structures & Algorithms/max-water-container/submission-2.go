func maxArea(heights []int) int {
	area := func(a, b int) int {
		if heights[a] > heights[b] {
			return heights[b] * (b - a)
		} else {
			return heights[a] * (b - a)
		}
	}
	i := 0
	j := len(heights) - 1
	mr := 0
	for i < j {
		if area(i, j) > mr {
			mr = area(i, j)
		}
		if area(i, j-1) > mr {
			mr = area(i, j-1)
			j--
		} else if area(i+1, j) > mr {
			mr = area(i+1, j)
			i++
		} else {

			if heights[i] > heights[j] {
				j--
			} else {
				i++
			}
		}

	}
	return mr
}