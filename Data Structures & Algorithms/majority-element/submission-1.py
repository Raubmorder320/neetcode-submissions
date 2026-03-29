class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            y = nums.count(v)
            if y>len(nums)//2:
                return v