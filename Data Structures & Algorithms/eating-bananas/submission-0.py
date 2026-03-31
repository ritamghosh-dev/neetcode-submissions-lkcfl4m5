class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=0
        while l<r:
            mid=l+(r-l)//2
            counter=0
            for item in piles:
                counter+=math.ceil(item/mid)
            if counter>h:
                l=mid+1
            elif counter<=h:
                ans=mid
                r=mid
        if ans==0:
            return max(piles)
        return ans
        

