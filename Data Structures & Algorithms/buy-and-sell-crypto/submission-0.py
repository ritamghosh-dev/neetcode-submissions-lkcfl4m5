class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans=0
        for l in range(len(prices)-1):
            for r in range(l+1,len(prices)):
                if prices[r]-prices[l]>ans:
                    ans=prices[r]-prices[l]
        return ans