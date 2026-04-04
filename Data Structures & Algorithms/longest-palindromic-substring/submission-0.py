class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        start = 0
        length = 1
        for i in range(n):
            dp[i][i]=True
        for i in range(n):#column
            for j in range(i):#row
                if s[i] != s[j]:
                    continue
                elif j+1==i or j+2==i or dp[j+1][i-1]:
                    dp[j][i]= True
                    if i-j+1 > length:
                        length = i-j+1
                        start = j
        return s[start:start+length]
        


