class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i, v in enumerate(nums):
            if not v in d.keys():
                d[v] = 0
        for i, v in enumerate(nums):
            d[v]+=1
            if d[v]>len(nums)//2:
                return v