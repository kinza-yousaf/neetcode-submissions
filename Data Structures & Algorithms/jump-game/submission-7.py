class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # forward jump by keeping track of maxReach
        maxReach = 0
        for i, num in enumerate(nums):
            if i <= maxReach:
                maxReach = max(maxReach, i + nums[i])
            else:
                return False
        return True