class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        n=len(height)
        def recursive(l,r):
            water=min(height[l],height[r])*(r-l-1)
            for k in range(l+1,r):
                water-=height[k]
            return water
        i=0
        while i<n-1:
            if height[i]>0:
                if i<n-1:
                    j=i+1
                    curr=height[j]
                    ind=j
                    while j<n and height[j]<height[i]:
                        if height[j]>=curr:
                            curr=height[j]
                            ind=j
                        j+=1
                    if j>=n:
                        j=ind
                    ans+=recursive(i, j)
                    i=j
            else:
                i+=1
        return ans
