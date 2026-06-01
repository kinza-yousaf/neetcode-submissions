class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = defaultdict(int)
        for char in s1:
            s1Counts[char] += 1
        for i, char in enumerate(s2):
            if char in s1:
                s2SubStr = s2[i: i + len(s1)]
                s2SubCounts = defaultdict(int)
                for c in s2SubStr:
                    s2SubCounts[c] += 1
                if s1Counts == s2SubCounts:
                    return True
        return False
