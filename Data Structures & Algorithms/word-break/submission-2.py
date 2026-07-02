class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)

        lastIdx = 0

        for i in range(n + 1):
            if not dp[i]:
                continue
            for word in wordDict:
                end = len(word) + i
                if end <= n and s[i: end] == word:
                    dp[end] = True
            
                
        print(dp)
        return dp[n]