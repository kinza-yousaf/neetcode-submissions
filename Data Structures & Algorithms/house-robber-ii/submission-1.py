class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n)
        dp2 = [0] * (n)
        for i in range(1, n):
            prev1 = dp1[i - 1] if i - 1 >= 0 else 0
            prev2 = dp1[i - 2] if i - 2 >= 0 else 0
            dp1[i] = max(prev1, prev2 + nums[i])
        

        for i in range(n - 1):
            prev1 = dp2[i - 1] if i - 1 >= 0 else 0
            prev2 = dp2[i - 2] if i - 2 >= 0 else 0
            dp2[i] = max(prev1, prev2 + nums[i])

        return max(dp1[n - 1], dp2[n - 2]) if n > 1 else nums[0]