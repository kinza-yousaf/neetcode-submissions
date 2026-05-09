class Solution:

    def encode(self, strs: List[str]) -> str:
        return ",".join([str(len(s)) for s in strs]) + "*" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        sizes, sep, strs = s.partition("*")
        res = []
        if not sizes:
            return res
        for s in sizes.split(","):
            res.append(strs[:int(s)])
            strs = strs[int(s):]
        return res