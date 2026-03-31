class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        ans=[]

        def gen(openp,closedp):
            if openp==closedp==n:
                ans.append(''.join(stack))
                return
            if openp<n:
                stack.append('(')
                gen(openp+1,closedp)
                stack.pop(-1)
            if closedp<openp:
                stack.append(')')
                gen(openp,closedp+1)
                stack.pop(-1)
        gen(0,0)
        return ans
