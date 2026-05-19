class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        latestL = 0
        latestSubMap = {}
        longestL = 0
        for i, c in enumerate(s):
            if c not in latestSubMap:
                latestSubMap[c] = i
                latestL += 1
            else:
                idx = latestSubMap[c]
                latestSubMap = {k:v for k, v in latestSubMap.items() if v > idx}
                longestL = max(longestL, latestL)
                latestSubMap[c] = i
                latestL = len(latestSubMap)
        longestL = max(longestL, latestL)
        return longestL