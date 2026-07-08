class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # global map of latest character occurences
        mp = {}

        # left, right pointers for current window without repetitions
        l = 0
        res = 0
        for r, c in enumerate(s):
            if c in mp:
                l = max(mp[c] + 1, l) # since this mp[c] might have already fallen out of the window

            mp[c] = r # do it without else to store latest occurence
            res = max(res, r - l + 1) 
        return res