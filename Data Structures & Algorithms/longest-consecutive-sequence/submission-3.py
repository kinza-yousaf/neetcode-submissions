class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i, num in enumerate(nums):
            if num - 1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    length += 1
                    num += 1
                res = max(res, length)
        return res