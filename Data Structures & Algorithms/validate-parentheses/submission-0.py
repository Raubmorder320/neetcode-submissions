class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in val.values():
                stack.append(s[i])
                continue
            elif len(stack) > 0 and s[i] in val.keys() and val[s[i]] == stack[-1]:
                stack.pop(-1)
                continue
            return False
  
        if len(stack)==0:
            return True
        else:
            return False