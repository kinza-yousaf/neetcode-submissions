class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            if i - 1 >= 0: 
                prev = dp[i - 1]
            if i - 2 >= 0: 
                prev2 = dp[i - 2]
            dp[i] = max(prev, prev2 + num)
            
        print(dp)
        return dp[n-1]