import operator
from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,}
        for item in tokens:
            if item in ['+', '-', '*']:
                v1=stack.pop(-1)
                v2=stack.pop(-1)
                stack.append((operator_map[item](v2,v1)))
            elif item=="/":
                v1=stack.pop(-1)
                v2=stack.pop(-1)
                if v2/v1>=0:
                    stack.append(v2//v1)
                else:
                    stack.append(ceil(v2/v1))
            else:
                stack.append(int(item))
        return stack[-1]