class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        res = nums[0]
        maxP, minP = nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            candidates = [num, num * maxP, num * minP]
            maxP = max(candidates)
            minP = min(candidates)
            res = max(res, maxP)
        print(dp)
        return res