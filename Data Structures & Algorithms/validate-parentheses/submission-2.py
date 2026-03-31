    
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
            i=st.peek()
            if i not in dir or dir[i]!= char:
                st.push(char)
            else:
                st.pop()
        return st.isEmpty()
    


    
