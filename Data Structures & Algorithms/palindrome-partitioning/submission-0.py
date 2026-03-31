class Solution:
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
    
    def partition(self, s):
        ans = []
        n = len(s)

        def recur(st,stack):
            if st == n:
                ans.append(stack.copy())
                return 
            for i in range(st, n):
                if self.isPalindrome(s[st:i+1]):
                    stack.append(s[st:i+1])
                    recur(i+1,stack)
                    stack.pop()
        recur(0,[])
        return ans