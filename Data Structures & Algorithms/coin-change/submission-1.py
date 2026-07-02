class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        n = amount
        coinSet = set(coins)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i in coinSet:
                dp[i] = 1
            else:
                minCoins = float("inf")
                for coin in coins:
                    if i - coin > 0 and dp[i - coin] > 0:
                        minCoins = min(minCoins, 1 + dp[i - coin])
                dp[i] = minCoins if minCoins != float("inf") else -1
        
        print(dp)
        return dp[n] 