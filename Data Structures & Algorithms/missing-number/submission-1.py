class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i, num in enumerate(nums):
            xor = xor ^ num ^ i
        return xor ^ len(nums)