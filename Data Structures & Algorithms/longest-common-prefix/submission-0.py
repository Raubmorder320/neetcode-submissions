class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        minL = len(strs[0])
        i = 0
        while i < minL and strs[0][i] == strs[-1][i]:
            i +=1
        return strs[0][:i]