class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if stack and stack[-1][1] < temp:
                while stack and stack[-1][1] < temp:
                    ind, old_temp = stack.pop()
                    ans[ind] = i-ind
            stack.append((i,temp))
        # while stack:
        #     ind, old_temp = stack.pop()
        #     ans[ind]=0
        return ans
                

            