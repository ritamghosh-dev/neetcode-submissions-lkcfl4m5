class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tracker=Counter(t)
        window_tracker=collections.defaultdict(int)
        def is_valid(window_tracker,tracker):
            temp=True
            for key in tracker.keys():
                if tracker[key]>window_tracker[key]:
                    temp=False
                    break
            return temp
        l=0
        ans="0"*(len(s)+1)
        for i in range(len(s)):
            if s[i] not in tracker:
                l+=1
            else:
                break
        r=l-1
        while r <len(s)-1:
            while r <len(s)-1 and not is_valid(window_tracker, tracker):
                r+=1
                window_tracker[s[r]]+=1
            while is_valid(window_tracker,tracker) :
                if len(ans)>r-l+1:
                    ans=s[l:r+1]
                window_tracker[s[l]]-=1
                l+=1
        if ans=="0"*(len(s)+1):
            return ""
        return ans
                
                
                

            

        