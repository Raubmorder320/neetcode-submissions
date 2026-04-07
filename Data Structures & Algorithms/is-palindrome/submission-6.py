class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.split()).lower()
        c=''
        for i in range(len(s)):
            if s[i].isalnum():
                c+=s[i]
        return c==c[::-1]