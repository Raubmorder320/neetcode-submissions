class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        s = []
        for i in range(len(strs)):
            w = ''.join(sorted(strs[i]))

            if w not in dic:
                dic[w] = []

        for k in range(len(strs)):
            dic[''.join(sorted(strs[k]))].append(strs[k])
        for i in dic.values():
            s.append(i)
        return s