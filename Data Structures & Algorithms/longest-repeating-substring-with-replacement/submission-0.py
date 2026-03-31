class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker=collections.defaultdict(int)
        L=0
        s=list(s)
        ans=-1
        for R in range(len(s)):
            tracker[s[R]]+=1
            while (R-L+1)-max(tracker.values())>k:
                tracker[s[L]]-=1
                L+=1
            
            ans=max(ans,R-L+1)
        if ans==-1:
            return 1
        else:
            return ans