class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                    return nums[l]
            mid = (l + r) // 2
            # left sorted
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                # right sorted
                r = mid
        return nums[l]