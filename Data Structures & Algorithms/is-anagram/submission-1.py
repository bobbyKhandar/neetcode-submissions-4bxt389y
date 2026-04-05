class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=[0]*26
        y=[0]*26
        for c in s:
            x[ord(c)-97]+=1
        for c in t:
            y[ord(c)-97]+=1
        return x==y