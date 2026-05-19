class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c.lower()) - ord('a')] += 1
            res[tuple(k)].append(s)
        print(list(res.values()))
        return list(res.values())