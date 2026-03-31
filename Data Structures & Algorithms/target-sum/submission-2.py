class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for key, value in dp.items():
                next_dp[key + num] += value
                next_dp[key - num] += value
            dp = next_dp
        return dp[target]