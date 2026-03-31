class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        s=list(s)
        window=[]
        ans=-float("inf")
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L+=1
            
            else:
                window.append(s[R])
                ans=max(ans,R-L+1)
        if ans==-float("inf"):
            return 0
        else:
            return ans