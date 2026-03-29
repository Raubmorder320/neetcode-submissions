from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)-1
        d = defaultdict(int)

        for i, v in enumerate(nums):
            d[v]+=1
        nums[:] = [0]*d[0]+[1]*d[1]+d[2]*[2]
        