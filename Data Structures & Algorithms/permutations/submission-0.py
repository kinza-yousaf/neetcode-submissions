class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, remaining):
            if not remaining:
                res.append(curr.copy())
            for n in remaining:
                curr.append(n)
                dfs(curr, [x for x in remaining if x != n])
                curr.pop()


        
        dfs([], nums)
        return res