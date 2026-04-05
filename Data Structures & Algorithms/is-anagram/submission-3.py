class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        x=[0]*26
        for c in s:
            x[ord(c)-97]+=1
        for c in t:
            x[ord(c)-97]-=1
        return x==[0]*26