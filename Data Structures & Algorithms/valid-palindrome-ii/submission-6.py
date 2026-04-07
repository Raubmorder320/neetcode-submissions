class Solution:
    def validPalindrome(self, s: str) -> bool:
        c=0
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                c+=1
                if s[l+1]==s[r]:
                    l+=1
                elif s[l]==s[r-1]:
                    r-=1
                else:
                    c+=1
                    l+=1
                    r-=1
                if c==2:
                    return False
        return True