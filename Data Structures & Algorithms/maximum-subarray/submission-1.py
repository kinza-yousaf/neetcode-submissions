class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        res = prev
        for i in range(1, n):
            num = nums[i]
            res = max(res, max(prev + num, num))
            prev = max(prev + num, num)
        return res
