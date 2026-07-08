class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n)
        dp[n - 1] = True
        if n == 1:
            return True
        for i in range(n - 2, -1, -1):
            jump = nums[i]
            while jump > 0:
                if i + jump >= n or dp[i + jump]:
                    dp[i] = True
                jump -= 1
        print(dp)
        return dp[0]