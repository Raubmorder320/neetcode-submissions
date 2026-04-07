class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split()
        s = ''.join(s).lower()
        s=''.join(s.split('?'))
        s=''.join(s.split(','))
        s=''.join(s.split('\''))
        s=''.join(s.split('.'))
        s=''.join(s.split(':'))

        
        s.strip()
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1 
            r-=1
        return True