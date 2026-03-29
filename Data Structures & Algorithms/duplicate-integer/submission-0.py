class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i, n in enumerate(nums):
            if n in a:
                return True
            a.add(n)
        return False