class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        d = defaultdict(int)
        answer = 0
        d[0]=1
        for i in range(len(nums)):
            pref_sum+=nums[i]
            if pref_sum-k in d:
                answer+=d[pref_sum-k]
            d[pref_sum] += 1 



        return answer
