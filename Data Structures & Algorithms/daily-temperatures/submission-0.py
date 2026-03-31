class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0 for num in temperatures]
        for num in enumerate(temperatures):
            while stack and stack[-1][1]<num[1]:
                temp=stack.pop(-1)
                ans[temp[0]]=num[0]-temp[0]
            stack.append(num)
        while stack:
            temp=stack.pop(-1)
            ans[temp[0]]=0
        return ans