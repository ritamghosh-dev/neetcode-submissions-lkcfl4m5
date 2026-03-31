class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary = len(s), set(dictionary)
        cache = {n:0}
        def dp(start):
            if start in cache:
                return cache[start]
            ans = 1 + dp(start + 1)
            for end in range(start, n):
                curr = s[start: end +1]
                if curr in dictionary:
                    ans = min(ans, dp(end + 1))
            cache[start] = ans
            return ans
        return dp(0)