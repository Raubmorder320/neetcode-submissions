class Solution:
    
    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in range(len(strs)):
            s += str(len(strs[i]))+'#'+strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        i=1
        l = ''
        a = []
        while i<len(s):
            l+=s[i-1]

            if s[i]=="#":
                if l=='0':
                    a.append('')
                    i+=1
                else:
                    a.append(s[i+1:i+int(l)+1])
                    i+=int(l)+1
                    l=''
            i+=1
        return a