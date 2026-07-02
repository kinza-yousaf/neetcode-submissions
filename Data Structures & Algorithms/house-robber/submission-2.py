class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev1, prev2, res = 0, 0, 0
        for i, num in enumerate(nums): 
            res = max(prev1, prev2 + num)
            prev1, prev2 = res, prev1 
        return res