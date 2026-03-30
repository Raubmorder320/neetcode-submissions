from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        answer = set()
        for i in range(len(nums)):
            d[nums[i]]+=1
            if d[nums[i]]> len(nums)//3:
                answer.add(nums[i])
        return list(answer)