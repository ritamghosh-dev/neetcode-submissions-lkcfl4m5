class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tracker={}
        def recur(i):#Returns the min cost from this index onwards
            if i in tracker:
                return tracker[i]
            if i==len(cost)-1:
                return cost[i]
            if i>=len(cost):
                return 0
            res=cost[i]
            if i+1 in tracker:
                temp1=tracker[i+1]
            else:
                temp1=recur(i+1)
            if i+2 in tracker:
                temp2=tracker[i+2]
            else:
                temp2=recur(i+2)
            res+=min(temp1,temp2)
            tracker[i]=res
            return res
        return min(recur(0),recur(1))

