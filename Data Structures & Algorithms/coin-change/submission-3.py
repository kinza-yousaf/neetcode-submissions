class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if coin == a:
                    dp[a] = 1
                else:
                    if a - coin >= 0:
                        dp[a] = min(1 + dp[a - coin], dp[a])
        return dp[amount] if dp[amount] < float("inf") else -1