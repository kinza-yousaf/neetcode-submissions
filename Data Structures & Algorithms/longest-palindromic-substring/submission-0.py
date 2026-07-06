class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 1
        maxS = ""

        for i in range(len(s)):
            # odd centered
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > maxL:
                maxL = max(maxL, r - l + 1)
                maxS = s[l + 1: r]
            # even centered
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > maxL:
                maxL = max(maxL, r - l + 1)
                maxS = s[l + 1: r]
        return maxS

            

        