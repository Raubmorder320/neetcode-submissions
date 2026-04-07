class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        flag = True
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                l1=l
                r1=r
                while l1+1<=r1:
                    if s[l1+1]!=s[r1]:
                        flag = False
                    l1+=1
                    r1-=1
                while l<=r-1:
                    if s[l]!=s[r-1]:
                        return flag
                    l+=1
                    r-=1
        return True