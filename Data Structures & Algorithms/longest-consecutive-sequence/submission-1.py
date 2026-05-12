class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i, num in enumerate(nums):
            num = nums[i]
            # identify the start of sequence
            length = 1
            if num-1 not in numSet:
                while num + 1 in numSet:
                    length += 1
                    num += 1
            longest = max(longest, length)
        return longest