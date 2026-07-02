class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robSlice(houses):
            n = len(houses)
            prev1, prev2, res = 0, 0, 0
            for i, num in enumerate(houses): 
                res = max(prev1, prev2 + num)
                prev1, prev2 = res, prev1 
            return res
        
        return max(robSlice(nums[1:]), robSlice(nums[: n - 1]))