class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            num = nums[i]
            dp[i] = max(dp[i - 1] + num, num)
            res = max(res, dp[i])
        print(dp)
        return res
