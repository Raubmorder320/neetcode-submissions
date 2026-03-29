class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        forward = [nums[0]]+[1 for _ in range(len(nums)-1)]
        backward = [nums[-1]]+[1 for _ in range(len(nums)-1)]
        for i in range(1,len(nums)):
            forward[i] = forward[i-1]*nums[i]
        forward = [1]+forward
        for i in range(1,len(nums)):
            backward[i] = backward[i-1]*nums[len(nums)-i-1]
        backward = backward+[1]
        for i in range(len(nums)):
            ans[i] = forward[i]*backward[len(nums)-i-2]
        return ans