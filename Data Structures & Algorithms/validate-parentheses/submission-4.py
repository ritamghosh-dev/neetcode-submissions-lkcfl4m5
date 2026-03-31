    
class Stack:
    def __init__(self):
        self.st=[]
    def push(self,item):
        self.st.append(item)
    def pop(self):
        if len(self.st)!=0:
            return self.st.pop()
    def peek(self):
        if len(self.st)!=0:
            return self.st[-1]
    def isEmpty(self):
        if len(self.st)==0:
            return True
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        dir={'{':'}','[':']','(':')'}
        l=list(s)
        st=Stack()
        for char in l:
            if st.peek() in dir and dir[st.peek()]==char:
                st.pop()
            else:
                st.push(char)
            # if st.peek() not in dir or dir[st.peek()]!= char: #We will push
            #     st.push(char)
            # else:
            #     st.pop()
        return st.isEmpty()
    


    
