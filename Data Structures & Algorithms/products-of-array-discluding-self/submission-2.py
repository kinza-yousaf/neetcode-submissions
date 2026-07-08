class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1] * len(nums)
        postProd = [1] * len(nums)
        pre, post = 1, 1
        l, r = 0, len(nums) - 1
        while l < len(nums) and r >= 0:
            preProd[l] = pre 
            postProd[r] = post
            pre *= nums[l]
            post *= nums[r]

            l += 1
            r -= 1
        return [pre * prod for pre, prod in list(zip(preProd, postProd))]