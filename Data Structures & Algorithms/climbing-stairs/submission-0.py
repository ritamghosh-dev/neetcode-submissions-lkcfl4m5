class Solution:
    def climbStairs(self, n: int) -> int:
        tracker={}
        def dp(curr):
            if curr in tracker:
                return tracker[curr]
            if curr>=n-1 :
                return 1
            if n-curr==2:
                return 2
            if curr+1 in tracker:
                temp1=tracker[curr+1]
            else:
                temp1=dp(curr+1)
            if curr+2 in tracker:
                temp2=tracker[curr+2]
            else:
                temp2=dp(curr+2)
            tracker[curr]=temp1+temp2
            return tracker[curr]
        return dp(0)
