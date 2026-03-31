class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ans=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                tempi,temph=stack.pop()
                start=tempi
                ans=max(ans,temph*(i-tempi))
            stack.append((start,h))
        while stack:
            tempi,temph=stack.pop()
            ans=max(ans,temph*(len(heights)-tempi))
        return ans