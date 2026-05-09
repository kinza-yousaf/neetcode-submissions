class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        for i, num in enumerate(nums):
            if i > 0:
                left_products[i] = left_products[i-1] * nums[i-1]

        reversed_nums = list(reversed(nums))
        for j, num in enumerate(reversed_nums):
            right_products[j] = reversed_nums[j] if j == 0 else right_products[j-1] * reversed_nums[j]
        outs = [1] * len(nums)

        print(left_products)
        print(right_products)
        
        for i, num in enumerate(left_products):
            if i == len(nums) - 1:
                outs[i] = left_products[i]
            else: 
                outs[i] = left_products[i] * list(reversed(right_products))[i + 1]
        return outs