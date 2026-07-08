class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # try doing with pointers
        arr = [(nums[i], i) for i, num in enumerate(nums)]
        arr.sort()
        print(arr)
        l, r = 0, len(arr) - 1
        while l <= r:
            i, j = arr[l][1], arr[r][1]
            sum_ = arr[l][0] + arr[r][0]
            if sum_ == target:
                return [i, j] if i < j else [j, i]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        return []