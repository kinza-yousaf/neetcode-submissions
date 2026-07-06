class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        power = 0
        offset = 1
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                dp[i] = 1
                offset = 1
            else:
                dp[i] = 1 + dp[offset]
                offset += 1
        return dp

            
