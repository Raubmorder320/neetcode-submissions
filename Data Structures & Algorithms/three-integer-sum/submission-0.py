class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sums = []
        nums.sort()

        for i, v in enumerate(nums):
            l = i+1
            r = len(nums)-1
            if i!=0 and nums[i-1]==v:
                continue
            while l<r:
                if v + nums[l] + nums[r] > 0:
                    r -= 1
                elif v + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    sums.append([v, nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        return sums
        