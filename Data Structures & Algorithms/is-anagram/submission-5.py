class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnts = [0] * 26
        for i in range(len(s)):
            cnts[ord(s[i]) - ord('a')] += 1
            cnts[ord(t[i]) - ord('a')] -= 1
        for cnt in cnts:
            if cnt != 0:
                return False
        return True