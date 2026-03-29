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
        for i, v in enumerate(matrix):
            if search(v, target) != -1:
                return True
        return False