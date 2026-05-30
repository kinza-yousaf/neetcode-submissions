class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # i am thinking of left and right max to know at a certain point whether there will be a boundary on left or right
        
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(min(leftMax, rightMax) - height[l], 0)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(min(leftMax, rightMax) - height[r], 0)
        return res
            

        