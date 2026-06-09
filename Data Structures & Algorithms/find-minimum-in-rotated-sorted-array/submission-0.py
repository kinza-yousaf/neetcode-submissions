class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] == nums[r] or nums[r] > nums[l]:
            return nums[l]
        else:
            while nums[l] < nums[l + 1] and l + 1 < len(nums):
                l += 1
            return nums[l + 1] 