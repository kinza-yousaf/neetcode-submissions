class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            prev1 = dp[i-1] if i >= 1 else 0
            prev2 = dp[i-2] if i >= 2 else 0
            dp[i] = max(prev1, prev2 + num)
            
        print(dp)
        return dp[n-1]