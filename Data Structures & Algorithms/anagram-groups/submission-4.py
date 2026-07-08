class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            tup = tuple(k)
            anagrams[tup].append(s)
        return list(anagrams.values())