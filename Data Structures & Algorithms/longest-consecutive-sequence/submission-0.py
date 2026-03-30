class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l=0
        for i in range(len(nums)):
            if nums[i]-1 in s:
                continue         
            j = 0
            while nums[i]+j in s:
                j+=1
            l = max(j,l)
        return l
