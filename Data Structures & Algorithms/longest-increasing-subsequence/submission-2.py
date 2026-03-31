class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            curr = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = max(curr, 1 + dp[j])
            dp[i] = curr
        return max(dp)