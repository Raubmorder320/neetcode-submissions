class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):

            y = target - nums[i]
            if y in dic:
                return [dic[y], i]
            dic[v] = i
        