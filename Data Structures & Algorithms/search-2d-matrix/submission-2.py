class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            l = 0
            r = len(nums)-1
            while l<=r:
                m = (r+l)//2
                if nums[m]<target:
                    l = m+1
                elif nums[m]>target:
                    r = m-1
                else:
                    return m
            return -1
        l = 0
        r = len(matrix)-1
        while l <= r:
            m = (r+l)//2
            nums = matrix[m]
            if matrix[m][-1]<target:
                l = m+1
            elif matrix[m][0]>target:
                r = m-1
            else:
                break
        return search(nums, target) != -1